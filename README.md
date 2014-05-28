ProjectManager
==============

Project Management Application for MVSport Co.  Built with Django on an Amazon EC2 instance.

There are two branches: master, and Production.  The master branch is meant to contain the most recent code, no matter the environment for which is is meant.  Production is meant to contain the most recent production-ready code.  

There are effectively two differences between development and production code:
1) settings.py: there are two versions of the DATABASE tuple.  Instructions are in comments.
2) views.py: there are two versions of URL_ROOT.  Just comment in the right one.

Deployment Instructions:
    1) Log into ec2-user@54.86.250.252
    2) Navigate to /var/www/ProjectManager
    3) Pull from Production
    4) run:
          chown ec2-user:www db.sqlite3
          chmod 777 db.sqlite3
        in order to prepare the database
    5) run:
          sudo service httpd restart
        in order to restart the server
    
The site is currently live at ec2-54-86-250-252.compute-1.amazonaws.com
Admin is at ec2-54-86-250-252.compute-1.amazonaws.com/admin

It case it ever becomes an issue, httpd.conf is at etc/httpd/conf.  
