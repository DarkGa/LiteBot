from flask import Flask, render_template, request
from sys import version_info
from core.loader import loader
from core.utils import utils
from multiprocessing import Process as pt
import os, sys

web = Flask(__name__)

@web.route("/")
def main():
    return render_template("index.html")
   
@web.route("/modules")
def modules():
	modules_list=""
	for module in loader.modules():
		md=loader.load(module[1:]).Main
		try: ver=md.version
		except: ver="Unknown"
		try: info=md.info.replace("\n", "<br>")
		except: info="Unknown"
		try: conf=md.data
		except: conf=False
		if conf: configure=f'''<a class="btn btn-rounded btn-info btn-sm" href="/configure?name={module[1:]}" type="button">Настройка</a>'''
		else: configure=''
		
		modules_list+=f'''
		<li style="display: flex; align-items: center; justify-content: center; flex-direction: column;" class="list-group-item">
			<h4><span class="badge badge-info">Название:</span> {module[1:]}</h4>
			<p><span class="badge badge-info">Версия:</span> {ver}</p>
			<p><span class="badge badge-info">Информация:</span> {info}</p>
			{configure}
			<a class="btn btn-rounded btn-danger btn-sm" onclick="delModule('{module[1:]}')" type="button">Удалить</a>
		</li>
		'''
	return render_template("modules.html", m_list=modules_list)

@web.route("/panel")
def panel():
    return render_template("panel.html", modules=len(loader.modules()), python_v=f"{version_info.major}.{version_info.minor}.{version_info.micro} {version_info.releaselevel}")

@web.route("/stop_web")
def stop_web():
	utils.buffer.write(["web_panel", False])
	os._exit(9)

@web.route("/configure_complete")
def cc():
	table=request.args.get('table')
	column=request.args.get('column')
	data=request.args.get('data')
	try: utils.db.select(table, column); exits=True
	except: exits=False
	if not exits:
		try: utils.db.create_table(table, column); new=True
		except: utils.db.add_table(table, column); new=False
	else: new=False
	
	if not new: utils.db.update(table, column, data); return f"Конфигурация модуля была обновлена"
	else: utils.db.insert_into(table, column, data); return f"Конфигурация модуля была создана"

@web.route("/configure")
def configure():
	module = request.args.get('name')
	md = loader.load(module).Main
	try: ver=md.version
	except: ver="Unknown"
	try: info=md.info.replace("\n", "<br>")
	except: info="Unknown"
	
	forms=''
	for form in md.data:
		forms+=f'''
<form style="display: flex; align-items: center; justify-content: center; flex-direction: column;" onsubmit="return false;" id="{form}" class="md-form">
<input type="text" id="{form}" class="form-control">
  <label for="{form}">{form}</label>
  <button class="btn btn-info" onclick='config("{module}", "{form}")'>Сохранить</button>
</form>
		'''
	
	template=f'''
        <div class="row">
            <div class="col-sm">
                <div class="card bg-primary">
                    <div class="card-header text-white">
                        Информация
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item"><span class="badge badge-info">Название:</span> {module}</li>
                        <li class="list-group-item"><span class="badge badge-info">Версия:</span> {ver}</li>
                        <li class="list-group-item"><span class="badge badge-info">Информация:</span> {info}</li>
                    </ul>
                  </div>
            </div>
            <div style="margin-top: 20px; margin-bottom: 20px;" class="col-sm">
                
                <div class="card bg-primary">
                    <div style="text-align: center;" class="card-header text-white">
                        <h3>Настройки модуля</h3>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item" style="display: flex; align-items: center; justify-content: center; flex-direction: column;">{forms}</li>
                    </ul>
                </div>
            </div>
        </div>
	'''
	return render_template("configure.html", module=template)
	
	

@web.route("/reload_modules")
def reload():
	for module in loader.modules():
		try: loader.reload(module)
		except: pass
	return "Модули успешно перезагружены!"

@web.route("/delete_module")
def delete():
	module = request.args.get('name')
	if "."+module in loader.modules():
		try: loader.unload("."+module)
		except: pass
		os.remove(f"modules/{module}.py")
		return f"Модуль '{module}' успешно удален."
	else: return f"Модуль '{module}' не обнаружен."
		
	

web.host='127.0.0.1'
web.use_evalex=False

def web_run(res):
	pt(target=web.run).start()
	