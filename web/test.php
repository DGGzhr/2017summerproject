<?php
$mysql_server_name='127.0.0.1'; 
 
$mysql_username='root'; 
 
$mysql_password='123456'; 
 
$mysql_database='time'; 
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ; 
mysql_select_db($mysql_database);


#$num=$_GET["num"];
#$num=6;
#$time=date('Y-m-d H:i:s');
#echo $time;
$sql="select  domain from domain where time between '2017-07-28 13:00:00' and '2017-07-28 14:30:00' group by domain";
$result = mysql_query($sql,$conn);
while($row = mysql_fetch_array($result))
{

$arr[] = array( 
        'domain' => $row['domain']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>
