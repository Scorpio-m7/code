<?php
$USR='admin';
$SALT='986cc033e62b473a0b56e4e52636b503b706fc45';
$site_full_name='GetSimple';
$site_version_no='3.3.15';
$name_url_clean=strtolower(str_replace(' ','-',$site_full_name));
$ver_no_clean=str_replace('.','',$site_version_no);
$cookie_name=strtolower($name_url_clean).'_cookie_'.$ver_no_clean;
$slatUSR=sha1($USR,$SALT);
$slatCOOKIE=sha1($cookie_name,$SALT);
echo $slatUSR;
echo "\n";
echo '2:',$slatCOOKIE;
?>