from flask import Flask, render_template, request
from sys import version_info
from core.loader import loader
from core.utils import utils
from multiprocessing import Process as pt
import os, sys, requests, json

web = Flask(__name__)

@web.route("/")
def main():
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	return render_template("index.html", all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])
   
@web.route("/modules")
def modules():
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	modules_list=""
	for module in loader.modules():
		try:
			md=loader.load(module[1:]).Main
			try: ver=md.version
			except: ver="Unknown"
			try: info=md.info.replace("\n", "<br>")
			except: info="Unknown"
			try: conf=md.data
			except: conf=False
			if conf: configure=f'''<a class="btn btn-rounded btn-{theme_loaded["all"]} btn-sm" href="/configure?name={module[1:]}" type="button">Настройка</a>'''
			else: configure=''
			
			modules_list+=f'''
			<li style="display: flex; align-items: center; justify-content: center; flex-direction: column; background-color: {theme_loaded['background']};" class="list-group-item">
				<h4><span class="badge badge-{theme_loaded["badges"]}">Название:</span> {module[1:]}</h4>
				<p><span class="badge badge-{theme_loaded["badges"]}">Версия:</span> {ver}</p>
				<p><span class="badge badge-{theme_loaded["badges"]}">Информация:</span> {info}</p>
				{configure}
				<a class="btn btn-rounded btn-danger btn-sm" onclick="delModule('{module[1:]}')" type="button">Удалить</a>
			</li>
			'''
		except:
			modules_list+=f'''
			<li style="display: flex; align-items: center; justify-content: center; flex-direction: column; background-color: {theme_loaded['background']};" class="list-group-item">
				<h4><span class="badge badge-{theme_loaded["badges"]}">Название:</span> {module[1:]}</h4>
				<p><span class="badge badge-{theme_loaded["badges"]}">Версия:</span> Unknown</p>
				<p><span class="badge badge-{theme_loaded["badges"]}">Информация:</span> Не удалось загрузить модуль, может зависимости не удовлетворены?</p>
				{configure}
				<a class="btn btn-rounded btn-danger btn-sm" onclick="delModule('{module[1:]}')" type="button">Удалить</a>
			</li>
			'''
	return render_template("modules.html", m_list=modules_list, all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])

@web.route("/store")
def store():
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	if request.args.get('module'): module=request.args.get('module'); opens=True
	else: opens=False
	if opens!=True:
		database=requests.get("https://raw.githubusercontent.com/DarkGa/LiteBot-store/main/database").text
		modules_list=''
		for module in database.split("\n"):
			config=requests.get(f"https://raw.githubusercontent.com/DarkGa/LiteBot-store/main/configs/{module}.json").json()
			try: ver=config["version"]
			except: ver="Unknown"
			try: info=config["info"].replace("\n", "<br>")
			except: info="Unknown"
			if len(config["logo"])!=0: logo=f"<img style='width: 100%;' src='https://github.com/DarkGa/LiteBot-store/raw/main/logo/{config['logo']}'>"
			else: logo=''
			modules_list+=f'''
			<li style="display: flex; align-items: center; justify-content: center; flex-direction: column; background-color: {theme_loaded['background']};" class="list-group-item">
			   {logo}
				<h4><span class="badge badge-{theme_loaded["badges"]}">Название:</span> {config["name"]}</h4>
				<p><span class="badge badge-{theme_loaded["badges"]}">Версия:</span> {ver}</p>
				<p><span class="badge badge-{theme_loaded["badges"]}">Информация:</span> {info}</p
				<li style="display: flex; align-items: center; justify-content: center; flex-direction: column;" class="list-group-item"><a class="btn btn-{theme_loaded["all"]}" href="/store?module={module}" type="button">Подробнее</a></li>
			</li>
			'''
		return render_template("store.html", m_list=modules_list, all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])
	else:
		config=requests.get(f"https://raw.githubusercontent.com/DarkGa/LiteBot-store/main/configs/{module}.json").json()
		try: ver=config["version"]
		except: ver="Unknown"
		try: info=config["info"].replace("\n", "<br>")
		except: info="Unknown"
		if len(config["update_info"]): updates=config["update_info"].replace("\n", "<br>")
		else: updates="*пусто*"
		if len(config["requirements"]): requirements=config["requirements"]
		else: requirements="Не требуются"
		if len(config["logo"])!=0: logo=f"<img style='background-color: {theme_loaded['background']}; width: 100%;' src='https://github.com/DarkGa/LiteBot-store/raw/main/logo/{config['logo']}'>"
		else: logo=''
		if not module+'.py' in os.listdir('modules'): install=f'''<a style="display: flex; align-items: center; justify-content: center; flex-direction: column;" class="btn btn-success" onclick="installModule('{module}'); document.location.reload();" type="button">Установить</a>'''
		else: install=f'''<a style="display: flex; align-items: center; justify-content: center; flex-direction: column;" class="btn btn-danger" onclick="delModule('{module}'); document.location.reload();" type="button">Удалить</a>'''
		template=f'''
        <div style="background-color: {theme_loaded['background']};" class="row">
		{logo}
            <div style=" background-color: {theme_loaded['background']}; margin-top: 20px;" class="col-sm">
			
                <div class="card bg-{theme_loaded['all']}">
                    <div class="card-header">
                        Информация
                    </div>
					{install}
                    <ul class="list-group list-group-flush">
					
                        <li style=" background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Название:</span> {module}</li>
                        <li style=" background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Версия:</span> {ver}</li>
                        <li style=" background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Информация:</span> {info}</li>
                        <li style=" background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Зависимости:</span> {requirements}</li>
                    </ul>
                  </div>
            </div>
            <div style="background-color: {theme_loaded['background']}; margin-top: 20px;" class="col-sm">
                
                <div class="card bg-{theme_loaded['all']}">
                    <div style="text-align: center;" class="card-header text-white">
                        <h3>Об обновлении</h3>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li style=" background-color: {theme_loaded['background']};" class="list-group-item">{updates}</li>
                    </ul>
                </div>
            </div>
        </div>
	'''
		return render_template("configure.html", module=template, all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])

@web.route("/theme")
def theme():
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	if request.args.get('them'): them=request.args.get('them'); opens=True; print(them)
	else: opens=False
	if opens!=True:
		themes=[theme for theme in os.listdir("web/theme") if theme.endswith(".json")]
		template=''
		for theme in themes:
			
			template+=f'''
			<div style="background-color: {theme_loaded["background"]}; margin-top: 20px;" class="card">
				<img src="/static/logo/{theme[:-5]}.png" class="card-img-top"/>
				<div class="card-body">
					<a class="btn btn-{theme_loaded["all"]}" onclick="changeTheme('{theme[:-5]}'); document.location.reload();" type="button">Применить</a>
				</div>
			</div>
			'''
		return render_template("store.html", m_list=template, all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])
	else:
		f=open("web/theme/settings/config.json", "w")
		them=f'"theme": "{str(them)}"'
		f.write("{"+them+"}")
		return "Тема была применена."
		
		

@web.route("/panel")
def panel():
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	return render_template("panel.html", modules=len(loader.modules()), python_v=f"{version_info.major}.{version_info.minor}.{version_info.micro} {version_info.releaselevel}", all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])

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
	on_theme=json.loads(open("web/theme/settings/config.json", "r").read())
	theme_loaded=json.loads(open("web/theme/"+on_theme["theme"]+".json", "r").read())
	module = request.args.get('name')
	md = loader.load(module).Main
	try: ver=md.version
	except: ver="Unknown"
	try: info=md.info.replace("\n", "<br>")
	except: info="Unknown"
	
	forms=''
	for form in md.data:
		forms+=f'''
<form style="background-color: {theme_loaded['background']}; display: flex; align-items: center; justify-content: center; flex-direction: column;" onsubmit="return false;" id="{form}" class="md-form">
<input type="text" id="{form}" class="form-control">
  <label for="{form}">{form}</label>
  <button class="btn btn-{theme_loaded['all']}" onclick='config("{module}", "{form}")'>Сохранить</button>
</form>
		'''
	
	template=f'''
        <div style="background-color: {theme_loaded['background']};" class="row">
            <div class="col-sm">
                <div class="card bg-{theme_loaded['all']}">
                    <div class="card-header text-white">
                        Информация
                    </div>
                    <ul class="list-group list-group-flush">
                        <li style="background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Название:</span> {module}</li>
                        <li style="background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Версия:</span> {ver}</li>
                        <li style="background-color: {theme_loaded['background']};" class="list-group-item"><span class="badge badge-{theme_loaded["badges"]}">Информация:</span> {info}</li>
                    </ul>
                  </div>
            </div>
            <div style="margin-top: 20px; margin-bottom: 20px;" class="col-sm">
                
                <div class="card bg-{theme_loaded['all']}">
                    <div style="text-align: center;" class="card-header text-white">
                        <h3>Настройки модуля</h3>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item" style="background-color: {theme_loaded['background']}; display: flex; align-items: center; justify-content: center; flex-direction: column;">{forms}</li>
                    </ul>
                </div>
            </div>
        </div>
	'''
	return render_template("configure.html", module=template, all=theme_loaded["all"], badges=theme_loaded["badges"], background=theme_loaded["background"], text=theme_loaded["text"])
	
	

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

@web.route("/install_module")
def install():
	module = request.args.get('module')
	print(module)
	r = requests.get("https://raw.githubusercontent.com/DarkGa/LiteBot-store/main/modules/"+module+".py")
	open("modules/"+module+".py", "w").write(r.text)
	return f"Модуль '{module}' успешно установлен."

		
	

web.host='127.0.0.1'
web.use_evalex=False

def web_run(res):
	pt(target=web.run).start()