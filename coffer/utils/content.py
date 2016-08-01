versions = ['karmic', 'wily', 'jessie-kfreebsd', 'sarge.buildd', 'maverick', 'oneiric', 'gutsy', 'quantal', 'hardy', 'jessie', 'precise', 'stretch', 'woody.buildd', 'dasyatis', 'utopic', 'lenny', 'jaunty', 'yakkety', 'warty.buildd', 'etch-m68k', 'oldstable', 'hoary', 'stable', 'warty', 'edgy', 'vivid', 'lucid', 'intrepid', 'woody', 'unstable', 'trusty', 'sarge.fakechroot', 'etch', 'xenial', 'breezy', 'feisty', 'wheezy', 'hoary.buildd', 'saucy', 'dapper', 'squeeze', 'natty', 'aequorea', 'sid', 'chromodoris', 'sarge', 'raring', 'bartholomea', 'potato', 'testing']

precise = """ 
#------------------------------------------------------------------------------#
#                            OFFICIAL UBUNTU REPOS                             #
#------------------------------------------------------------------------------#


###### Ubuntu Main Repos
deb http://01.archive.ubuntu.com/ubuntu/ precise main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ precise main restricted universe multiverse 

###### Ubuntu Update Repos
deb http://01.archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ precise-updates main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ precise-proposed main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ precise-backports main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ precise-updates main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ precise-proposed main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ precise-backports main restricted universe multiverse 

###### Ubuntu Partner Repo
deb http://archive.canonical.com/ubuntu precise partner
deb-src http://archive.canonical.com/ubuntu precise partner

###### Ubuntu Extras Repo
deb http://extras.ubuntu.com/ubuntu precise main
deb-src http://extras.ubuntu.com/ubuntu precise main

"""

trusty = """ 
#------------------------------------------------------------------------------#
#                            OFFICIAL UBUNTU REPOS                             #
#------------------------------------------------------------------------------#


###### Ubuntu Main Repos
deb http://01.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse 

###### Ubuntu Update Repos
deb http://01.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ trusty-proposed main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ trusty-security main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ trusty-updates main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ trusty-proposed main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ trusty-backports main restricted universe multiverse 

"""

wily = """ 
#------------------------------------------------------------------------------#
#                            OFFICIAL UBUNTU REPOS                             #
#------------------------------------------------------------------------------#


###### Ubuntu Main Repos
deb http://01.archive.ubuntu.com/ubuntu/ wily main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ wily main restricted universe multiverse 

###### Ubuntu Update Repos
deb http://01.archive.ubuntu.com/ubuntu/ wily-security main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ wily-updates main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ wily-proposed main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ wily-backports main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ wily-security main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ wily-updates main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ wily-proposed main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ wily-backports main restricted universe multiverse 

"""

xenial = """
#------------------------------------------------------------------------------#
#                            OFFICIAL UBUNTU REPOS                             #
#------------------------------------------------------------------------------#


###### Ubuntu Main Repos
deb http://01.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse 

###### Ubuntu Update Repos
deb http://01.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse 
deb http://01.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse 
deb-src http://01.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse 

"""

wheezy = """
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                    
#------------------------------------------------------------------------------#

###### Debian Main Repos
deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ wheezy main contrib non-free 

###### Debian Update Repos
deb http://security.debian.org/ wheezy/updates main contrib non-free 
deb http://ftp.us.debian.org/debian/ wheezy-proposed-updates main contrib non-free 
deb-src http://security.debian.org/ wheezy/updates main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ wheezy-proposed-updates main contrib non-free 

"""

jessie = """
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                    
#------------------------------------------------------------------------------#

###### Debian Main Repos
deb http://ftp.us.debian.org/debian/ jessie main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ jessie main contrib non-free 

###### Debian Update Repos
deb http://security.debian.org/ jessie/updates main contrib non-free 
deb http://ftp.us.debian.org/debian/ jessie-proposed-updates main contrib non-free 
deb-src http://security.debian.org/ jessie/updates main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ jessie-proposed-updates main contrib non-free 

"""

stretch = """
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                    
#------------------------------------------------------------------------------#

###### Debian Main Repos
deb http://ftp.us.debian.org/debian/ stretch main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ stretch main contrib non-free 

###### Debian Update Repos
deb http://security.debian.org/ stretch/updates main contrib non-free 
deb http://ftp.us.debian.org/debian/ stretch-proposed-updates main contrib non-free 
deb-src http://security.debian.org/ stretch/updates main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ stretch-proposed-updates main contrib non-free 

"""

sid = """
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                    
#------------------------------------------------------------------------------#

###### Debian Main Repos
deb http://ftp.us.debian.org/debian/ sid main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ sid main contrib non-free 

###### Debian Update Repos
deb http://security.debian.org/ sid/updates main contrib non-free 
deb http://ftp.us.debian.org/debian/ sid-proposed-updates main contrib non-free 
deb-src http://security.debian.org/ sid/updates main contrib non-free 
deb-src http://ftp.us.debian.org/debian/ sid-proposed-updates main contrib non-free 

"""

sources = {
    "precise":precise,
    "trusty":trusty,
    "wily":wily,
    "xenial":xenial,
    "wheezy":wheezy,
    "jessie":jessie,
    "stretch":stretch,
    "sid":sid,
}
architectures = {
    "32bit":"i386",
    "64bit":"amd64",
    "x86":"i386",
    "x86_64":"amd64",
    "i386":"i386",
    "amd64":"amd64",
}
