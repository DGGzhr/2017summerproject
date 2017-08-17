<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='smalldata';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);

$num=$_GET["num"];
$domain=$_GET["domain"];
$value=$_GET["value"];
$sql="update data  set value = '$value'  where num='$num' and domain ='$domain'";
$result = mysql_query($sql,$conn);
mysql_close($conn);
?>

