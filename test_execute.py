# import test_script
from test_script import test_script

# forming INFO
INFO = {    # log-in
            "USERNAME": "user@phptravels.com",
            "PASSWORD": "demouser",
        }

crawler = test_script()

crawler.run(INFO=INFO)