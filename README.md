## captiveflask
Developing extra captive portals for captiveflask plugins

### description 
the plugin captiveflask allow the Attacker mount a wireless access point which is used in conjuction with a web server and iptables traffic capturing rules to create the phishing portal. Users can freely connect to these networks without a password and will often be directed to a login page where a password is required before being allowed to browse the web.   

### What is Wireless Phishing?
Wireless phishing is any technique by which an attacker attempts to convince wireless network users to divulge sensitive information. As we previously mentioned the associated wireless network is generally open and access to network resources is mediated by a web application known as a captive portal. A captive portal is a web page accessed with a web browser that is displayed to newly connected users of a Wi-Fi network before they are granted broader access to network resources. Captive portals are commonly used to present a landing or log-in page which may require authentication, payment, acceptance of an end-user license agreement or an acceptable use policy, or other valid credentials that both the host and user agree to adhere by. (Wiki)
 

### Creating Captive Portal template
For the interested, we give a brief technical overview of the process of creating a phishing portal here. Example configuration files for creating a simple captive portal template to Wp3.
first of all you need to make a repository fork and add your plugin template. 

Example configuration files for creating a simple template.

``` python
# file => ExamplePlugin.py
from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C # import plugin class base

class ExamplePlugin(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'ExamplePlugin',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : ' the Author',
        'TemplatePath' : C.TEMPLATES_FLASK +'templates/ExamplePlugin',
        'StaticPath' : C.TEMPLATES_FLASK + 'templates/ExamplePlugin/static',
        'Preview' : 'plugins/captivePortal/templates/ExamplePlugin/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = Flase 
```

#### File architecture
``` bash
ExamplePlugin/
├── preview.png
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── main.css
│   │   ├── styles.css
│   │   └── util.css
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-1.11.1.min.js
│       └── main.js
└── templates
    ├── login.html
    └── login_successful.html

4 directories, 9 files
```

### Editing html files 

Set Up the Phishing your custom page login captive portal

**login.html**

``` html
<!DOCTYPE html>
<html >
<head>
<title>Authentification</title>
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/util.css') }}">
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body >
  <div >
    <!-- Page content -->
    <form method="POST" >
      Login:<br>
      <input type="text" name="login">
      <br>
      Password:<br>
      <input type="text" name="password">
      <br><br>
      <input type="submit" value="Sig up">
    </form>
  </div>
</body>
</html>

```
Set Up the Phishing your custom page login successful

**login_successful.html**

``` html
<!DOCTYPE html>
<html >
<head>
  <title>Authentification</title>
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/util.css') }}">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
  </head>
    <h1>Login successful</h1>
  </body>
</html>
```

now, you need to include inside **.config/wifipumpkin3/config/app/captive-portal.ini** the key *ExamplePlugin=false* in tag plugins.
``` ini
[plugins]
FlaskDemo=false
Login_v4=false
loginPage=false
DarkLogin=true
 # new key with my new plugin
ExamplePlugin=false 

```


### Add language into the guest portal

if want to create multiple language that allow the user to pick a different one, checkout!
In plugin ExamplePlugin.py change the bool var **ConfigParser** to True and override function **init_language**. look;

``` python
# file => ExamplePlugin.py
from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C # import plugin class base


class ExamplePlugin(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'ExamplePlugin',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : 'The Author',
        'TemplatePath' : C.TEMPLATES_FLASK +'templates/ExamplePlugin',
        'StaticPath' : C.TEMPLATES_FLASK +'templates/ExamplePlugin/static',
        'Preview' : 'plugins/captivePortal/templates/ExamplePlugin/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = True

    def init_language(self, lang):
        if (lang):
          if (lang.lower() != 'default'):
              self.TemplatePath = C.TEMPLATES_FLASK +'templates/ExamplePlugin/language/{}'.format(lang)
              return
          for key,value in self.meta.items():
              self.__dict__[key] = value

```

#### File architecture
``` bash
ExamplePlugin/
├── language
│   ├── En
│   │   └── templates
│   │       ├── login.html
│   │       └── login_successful.html
│   └── ptBr
│       └── templates
│           ├── login.html
│           └── login_successful.html
├── preview.png
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── main.css
│   │   ├── styles.css
│   │   └── util.css
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-1.11.1.min.js
│       └── main.js
└── templates
    ├── login.html
    └── login_successful.html

9 directories, 13 files
```
now, you need to include inside **captive-portal.ini** the keys.
``` ini
[plugins]
FlaskDemo=false
Login_v4=false
loginPage=false
DarkLogin=true
ExamplePlugin=false

# new section
[set_ExamplePlugin]  
# default language
Default=true
# english language
En=false
 #huer huer br
PtBr=false

```
#### Include File .py

after configure the file ExamplePlugin.py, you need to move from the directory **captiveflask** in root wifipumpkin3 folder **/wifipumpkin3/plugins/captiveflask**
as you can see on screenshot bellow:

![captivefolder](img/captiveportal_folder.png)

with file **ExamplePlugin.py** into captiveflask directory, you need to reinstall the tool, you have  to reinstall on version  the python installed, let's go:

``` bash
# for python3.7
$ sudo python3.7 setup.py install
# for python3.8
$ sudo python3.8 setup.py install
```
if you running on Kali linux and followed the guide how to install above, only need to:
``` bash
python3 setup.py install
```

#### Include the Templates

now, it very simples copy the folder **ExamplePlugin** to path **.config/wifipumpkin3/config/templates/**, the plugin will be listed and working fine for capture the credentails.

#### Enjoy 

now, you can choose to keep your custom version for yourself or send it to all wp3 users.

have fun! Hack the Planet