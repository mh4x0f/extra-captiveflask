# captiveportals
Extra captive portals for WiFi-Pumpkin plugins 

### description 
the plugin Captive-Portal allow the Attacker mount a wireless access point which is used in conjuction with a web server and iptables traffic capturing rules to create the phishing portal. Users can freely connect to these networks without a password and will often be directed to a login page where a password is required before being allowed to browse the web.   

### What is Wireless Phishing?
Wireless phishing is any technique by which an attacker attempts to convince wireless network users to divulge sensitive information. As we previously mentioned the associated wireless network is generally open and access to network resources is mediated by a web application known as a captive portal. A captive portal is a web page accessed with a web browser that is displayed to newly connected users of a Wi-Fi network before they are granted broader access to network resources. Captive portals are commonly used to present a landing or log-in page which may require authentication, payment, acceptance of an end-user license agreement or an acceptable use policy, or other valid credentials that both the host and user agree to adhere by. (Wiki)
 

### Creating Captive Portal template
For the interested, we give a brief technical overview of the process of creating a phishing portal here. Example configuration files for creating a simple captive portal template to WiFi-Pumpkin.
first of all you need to make a repository fork and add your plugin template. 

Example configuration files for creating a simple template.

``` python
# file => ExamplePlugin.py
from plugins.captivePortal.plugin import CaptiveTemplatePlugin # import plugin class base

class ExamplePlugin(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'ExamplePlugin',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : ' the Author',
        'TemplatePath' : 'templates/ExamplePlugin',
        'StaticPath' : 'templates/ExamplePlugin/static',
        'Preview' : 'plugins/captivePortal/templates/ExamplePlugin/preview.png'
    }

    def __init__(self):
        for key,value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = Flase   
```

#### File architecture
``` python
ExamplePlugin/
├── preview.png
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── main.css
│   │   ├── styles.css
│   │   └── util.css
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-1.11.1.min.js
│       └── main.js
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

now, you need to include inside **settings.ini** the key *ExamplePlugin=false* in tag plugins.
``` ini
[plugins]
Example=false
ExamplePlugin=false

[set_Example]
Default=true
En=false
PtBr=false

```


### Add language into the guest portal

if want to create multiple language that allow the user to pick a different one, checkout!
In plugin ExamplePlugin.py change the bool var **ConfigParser** to True and override function **init_language**. look;

``` python

from plugins.captivePortal.plugin import CaptiveTemplatePlugin


class ExamplePlugin(CaptiveTemplatePlugin):
    meta = {
        'Name'      : 'ExamplePlugin',
        'Version'   : '1.0',
        'Description' : 'Example is a simple portal default page',
        'Author'    : 'The Author',
        'TemplatePath' : 'templates/ExamplePlugin',
        'StaticPath' : 'templates/ExamplePlugin/static',
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
              self.TemplatePath = 'templates/ExamplePlugin/language/{}'.format(lang)
              return
          for key,value in self.meta.items():
              self.__dict__[key] = value      
        

```

#### File architecture
``` python
ExamplePlugin/
├── language
│   ├── En
│   │   └── templates
│   │       ├── login.html
│   │       └── login_successful.html
│   └── ptBr
│       └── templates
│           ├── login.html
│           └── login_successful.html
├── preview.png
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── main.css
│   │   ├── styles.css
│   │   └── util.css
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-1.11.1.min.js
│       └── main.js
└── templates
    ├── login.html
    └── login_successful.html

9 directories, 13 files
```
now, you need to include inside **settings.ini** the keys.
``` ini
[plugins]
Example=false
ExamplePlugin=false

[set_Example]
Default=true
En=false
PtBr=false

[set_ExamplePlugin]
Default=true
En=false
PtBr=false

```

#### Preview Image
A preview image can be displayed on tab captiv-portal. This image is specified using the `preview` parameter the class of plugin.
``` python
 'Preview' : 'plugins/captivePortal/templates/ExamplePlugin/preview.png'
```
now, the WiFi-Pumpkin should be show a preview for images the captive portal.

#### Enjoy 
have fun!
