yolo_shopping/
├── application/                  
│   ├── __init__.py                # The file to initialize the application relation
│   ├── config.py                   # The file to divide the setting of application
│   ├── lib/                          # The directory to store using library in application
        ├── __init__.py          # To use with `from application.lib import Xxxx`  from the application
│   │   ├── web_camera/       # The library to use webcam
│   │   └── yolo/                  # The library in YOLOv3
│   ├── static/
│   │   └── stylesheet/
│   │       └── index.css         # Stylesheet for index.html
│   ├── templates/
│   │   └── index.html           # Template for MVT
│   └── views.py                    # View in MVT
├── requirements.txt
└── run.py                            # Launching file
