from flask import Flask, request, render_template, redirect, url_for, abort, flash

app = Flask(__name__)
app.secret_key = 'une cle(token) : grain de sel(any random string)'

auteurs=[
    {'id':1,'nomAuteur':'Goscinny-Uderzo'},
    {'id':2,'nomAuteur':'Roba-Rosy'},
    {'id':3,'nomAuteur':'Herge'},
    {'id':4,'nomAuteur':'Franquin - Delporte'}
]
bandesDessinees=[
    {'id':1,'serieBD':'Astérix et Obélix', 'auteur_id':1, 'titre':'La serpe d or', 'tome':1, 'dateParution':'2005-10-09', 'prix':'7.5', 'image':'bd1.png'},
    {'id':2,'serieBD':'Astérix et Obélix', 'auteur_id':1, 'titre':'Asterix et les Goths', 'tome':'2', 'dateParution': '2011-10-10', 'prix':'10', 'image':'bd2.png'},
    {'id':3,'serieBD':'Astérix et Obélix', 'auteur_id':1, 'titre':'Asterix et les gladiateurs', 'tome':'3', 'dateParution': '2004-10-11', 'prix':'5', 'image':'bd3.png'},
    {'id':4,'serieBD':'Astérix et Obélix', 'auteur_id':1, 'titre':'Tour de Gaule d astérix', 'tome':'4', 'dateParution': '2005-09-10', 'prix':'8.5', 'image':'bd20.png'},
    {'id':5,'serieBD':'Astérix et Obélix', 'auteur_id':1, 'titre':'La zizanie', 'tome':'15', 'dateParution': '2014-09-10', 'prix':'15', 'image':'bd4.png'},
    {'id':6,'serieBD':'Boule et Bill', 'auteur_id':2, 'titre':'60 gags de Boule et Bill', 'tome':1, 'dateParution':'2010-10-11', 'prix':'10', 'image':'bd5.png'},
    {'id':7,'serieBD':'Boule et Bill', 'auteur_id':2, 'titre':'Papa maman, Boule et... moi', 'tome':'8', 'dateParution':'2005-10-11', 'prix':'10.5', 'image':'bd6.png'},
    {'id':8,'serieBD':'Boule et Bill', 'auteur_id':2, 'titre':'Une vie de chien !', 'tome':'9', 'dateParution':'2012-10-11', 'prix':'20', 'image':'bd7.png'},
    {'id':9,'serieBD':'Boule et Bill', 'auteur_id':2, 'titre':'Attention chien marrant !', 'tome':'10', 'dateParution':'2013-10-11', 'prix':'10', 'image':'bd8.png'},
    {'id':10,'serieBD':'Boule et Bill', 'auteur_id':2, 'titre':'Jeux de Bill', 'tome':'11', 'dateParution':'2014-10-11', 'prix':'20', 'image':'bd9.png'},
    {'id':11,'serieBD':'Tintin', 'auteur_id':3, 'titre':'Tintin au pays des Soviets', 'tome':'1', 'dateParution':'2005-10-11', 'prix':'10', 'image':'bd10.png'},
    {'id':12,'serieBD':'Tintin', 'auteur_id':3, 'titre':'Tintin au Congo', 'tome':'2', 'dateParution':'2011-07-11', 'prix':'10', 'image':'bd11.png'},
    {'id':13,'serieBD':'Tintin', 'auteur_id':3, 'titre':'Tintin en Amérique', 'tome':'3', 'dateParution':'2012-10-11', 'prix':'10', 'image':'bd12.png'},
    {'id':14,'serieBD':'Tintin', 'auteur_id':3, 'titre':'Les Cigares du pharaon', 'tome':'4', 'dateParution':'2005-10-13', 'prix':'20', 'image':'bd13.png'},
    {'id':15,'serieBD':'Tintin', 'auteur_id':3, 'titre':'Le lotus bleu', 'tome':'5', 'dateParution':'2014-10-13', 'prix':'20', 'image':'bd14.png'},
    {'id':16,'serieBD':'Gaston Lagaffe', 'auteur_id':4, 'titre':'Gare aux gaffes', 'tome':1, 'dateParution':'2010-12-03', 'prix':'10', 'image':'bd15.png'},
    {'id':17,'serieBD':'Gaston Lagaffe', 'auteur_id':4, 'titre':'Gala de gaffes', 'tome':'2', 'dateParution':'2012-09-06', 'prix':'10', 'image':'bd16.png'},
    {'id':18,'serieBD':'Gaston Lagaffe', 'auteur_id':4, 'titre':'Gaffes à gogo', 'tome':'3', 'dateParution':'2014-08-06', 'prix':'8', 'image':'bd17.png'},
    {'id':19,'serieBD':'Gaston Lagaffe', 'auteur_id':4, 'titre':'Gaffes en gros', 'tome':'4', 'dateParution':'2013-04-06', 'prix':'10', 'image':'bd18.png'},
    {'id':20,'serieBD':'Gaston Lagaffe', 'auteur_id':4, 'titre':'Les gaffes d un gars gonflé', 'tome':'5', 'dateParution':'2005-03-06', 'prix':'8', 'image':'bd19.png'}
]


@app.route('/')
def show_accueil():
    return render_template('layout.html')

@app.route('/auteur/show')
def show_auteur():
    #print(auteur)
    return render_template('auteurs/show_auteur.html', auteur=auteurs)

@app.route('/auteur/add', methods=['GET'])
def add_auteur():
    return render_template('auteurs/add_auteur.html')

@app.route('/auteur/add', methods=['POST'])
def valid_add_auteur():
    nom = request.form.get('nom', '')
    print(u'auteur ajouté , libellé :', nom)
    message = u'auteur ajouté , nom :'+nom
    flash(message, 'alert-success')
    return redirect('/auteur/show')

@app.route('/auteurs/delete', methods=['GET'])
def delete_auteur():
    id = request.args.get('id', '')
    print ("un auteur supprimé, id :",id)
    message=u'un auteur supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/auteur/show')

@app.route('/auteurs/edit', methods=['GET'])
def edit_auteur():
    id = request.args.get('id', '')
    nomAuteur = request.args.get('nomAuteur', '')     # comment passé plusieurs paramètres (clé primaire composés)
    id=int(id)
    nomAuteur = nomAuteur[id-2]
    return render_template('auteurs/edit_auteur.html', auteur=auteurs)

@app.route('/auteur/edit', methods=['POST'])
def valid_edit_auteur():
    nomAuteur = request.form.get('nomAuteur')
    id = request.form.get('id', '')
    print(u'auteur modifié, id: ',id, " nomAuteur :", nomAuteur)
    message=u'auteur modifié, id: ' + id + " nomAuteur : " + nomAuteur
    flash(message, 'alert-success')
    return redirect('/auteur/show')

@app.route('/bandesDessinees/show')
def show_bandesDessinees():
    # print(articles)
    return render_template('article/show_article.html', bandesDessinees=bandesDessinees)

@app.route('/bandesDessinees/add', methods=['GET'])
def add_bandesDessinees():
    return render_template('bandesDessinees/add_bandesDessinees.html', bandesDessinees=bandesDessinees)

@app.route('/bandesDessinees/add', methods=['POST'])
def valid_add_bandesDessinees():
    nom = request.form.get('nom', '')
    type_article_id = request.form.get('type_article_id', '')
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    print(u'article ajouté , nom: ', nom, ' - type_article_id :', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article ajouté , nom:'+nom + '- type_article_id :' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message, 'alert-success')
    return redirect('/bandesDessinees/show')


@app.route('/bandesDessinees/delete', methods=['GET'])
def delete_bandesDessinees():
    id = request.args.get('id', '')
    message=u'un article supprimé, id : ' + id
    flash(message, 'alert-warning')
    return redirect('/bandesDessinees/show')

@app.route('/bandesDessinees/edit', methods=['GET'])
def edit_bandesDessinees():
    id = request.args.get('id', '')
    id=int(id)
    bandesDessinee = bandesDessinees[id-1]
    return render_template('bandesDessinees/edit_bandesDessinees.html', bandesDessinees=bandesDessinees, auteur=auteurs)

@app.route('/bandesDessinees/edit', methods=['POST'])
def valid_edit_bandesDessinees():
    id = request.form.get('id', '')
    nom = request.form.get('nom', '')
    type_article_id = request.form.get('type_article_id')
    prix = request.form.get('prix', '')
    stock = request.form.get('stock', '')
    description = request.form.get('description', '')
    image = request.form.get('image', '')
    print(u'article modifié , nom : ', nom, ' - type_article_id :', type_article_id, ' - prix:', prix, ' - stock:', stock, ' - description:', description, ' - image:', image)
    message = u'article modifié , nom:'+nom + '- type_article_id :' + type_article_id + ' - prix:' + prix + ' - stock:'+  stock + ' - description:' + description + ' - image:' + image
    flash(message, 'alert-success')
    return redirect('/bandesDessinees/show')



if __name__ == '__main__':
    app.run()
