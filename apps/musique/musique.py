


@webapp.route('/get/musique/<file>')
@login_required
def send_musique(file):
	user = session["utilisateur"]
	return send_from_directory("nas/"+user+"/musique", file)

@webapp.route("/list/musique")
@login_required
def list_musique():
	user = session["utilisateur"]
	message = {"error": []}
	if os.path.isdir("nas/"+user+'/'):
		if os.path.isdir("nas/"+user+"/musique"):
			files = os.listdir("nas/"+user+"/musique")
			audio_files = []
			for file in files:
				filename, file_extension = os.path.splitext(file)
				for i in load_datas("extension") :
					if i["extension"] == file_extension:
						if "audio" in i["content-type"]:
							audio_files.append(file)
							break
		else:
			message["error"].append("Vous n'avez pas de dossier musique.")
	else :
		message["error"].append("Vous n'avez pas de dossier personel pour le nas.")
	return(Response(response=json.dumps(audio_files),status=200,mimetype="application/json"))


@webapp.route("/musique")
@login_required
@need_app_active
def index_musique():
	return render_template("apps/musique/index.html",datas=locals(),myapp=myapp)


## extention file from : https://www.sitepoint.com/web-foundations/mime-types-complete-list/