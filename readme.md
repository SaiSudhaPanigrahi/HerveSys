# Hervé | Documentation :

/!\ Toutes les commandes indiquées doivent être exécutées dans le dossier Hervé !

## Exécuter Hervé :

Pour exécuter Hervé utilisez la commande :

```shell
python3 __main__.py run [-h/--host] [IP] [-p/--port] [PORT]
```

## Les applications :

### Création d'une application :


Que les applications créées soient des applications web ou backend elles s'initialisent de la même façon. Pour en créer une, exécutez dans le dossier Hervé la commande :

```shell
python3 __main__.py creatapp [nom du packet]
```

Cette commande aura pour effet de poser certaines questions puis générer une application déjà installée dans Hervé. Seul l'utilisateur `sys` pourra utiliser l'application par défaut. Les utilisateurs devrons l'activée eux-mêmes.

#### Pendant le développement :

Durant la création de votre application il faudra se soumettre à certaines conventions.

```python

@webapp.route("/mynewapp")
@login_required
def index_mynewapp():
	"""
	Votre code
	"""
	return render_template("apps/mynewapp/index.html",datas=locals(),myapp=myapp)
```

Il sera indispensable de définir les arguments `datas` et `myapp` pour avoir un bon fonctionnement d'Hervé et de votre application :
Dans le cas contraire, Flask relèvera une erreur.

##### Définir un widget pour son application :

Pour définir un widget dans son application ajouter dans le manifest.json les valeurs `"[élément de la page] [url de la page]"` à la liste `widgets`.
Généralement les widgets sont des éléments déjà présent dans les templates. Si votre widget ne l'est pas, vous pouvez générer du HTML depuis python :

```python

@webapp.route("/url")
@login_required
def index_mynewapp():
	html = tag("div",
		class_ = "my_class",
			contenu=tag("p",
				contenu="Mon super text"
		)
	)
	return Response(response=html),status=200,mimetype="text/html")
```

Ainsi vous pourrez sélectionner votre widget de la sorte :

```json
...

"widgets":[
	".my_class /url"
],

...
```

##### Définir une tache périodique

```python
def mafonctionperiodique():
	print("Je fonctionne")

schedule.every(10).seconds().do(mafonctionperiodique)

```
Il est possible d'utiliser un décorateur mais il ne fera que rendre votre code plus sale.
Le code ci-dessous est l'équivalent de celui du dessus.

```python
decorator = schedule.every(10).seconds().do

@decorator
def mafonctionperiodique():
	print("Je fonctionne")

```

##### Définir une tache perpétuelle

Pour rendre une fonction perpétuelle, utilisez le décorateur `myapp.forever`

```python
@myapp.forever
def mafonctionperpetuel():
	print("Je fonctionne")
```
##### Définir une tache en arrière plant

Pour exécuter une fonction en background, utilisez le décorateur `myapp.in_thread`

```python
@myapp.in_thread
def mafonction():
	print("Je fonctionne en background")
```

### Exportation d'une application

Pour exporter votre application par exemple pour le store, exécutez la commande :

```python3 __main__.py exportapp [nom du packet] [path du dossier où exporter l'application] ```

Cette commande exportera votre application dans `[path du dossier où exporter l'application]` si l'application demandée existe. Le packet créé sera installable.

### Installer une application :

Pour installer une application, exécutez la commande :

```python3__main__.py installapp [path de l'application] ```

L'application devrait être installée si les arguments donnés ne sont pas erronés. Seul l'utilisateur `sys` pourra utiliser l'application par défaut. Les utilisateurs devrons l'activée eux-mêmes.