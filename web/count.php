<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='time';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);
$time1=date('Y-m-d');
$time2=date('Y-m-d H:i:s');

$sql = "select  count(*) as num  from domain  where time  between '$time1' and '$time2' ";
$result = mysql_query($sql,$conn);
$row=mysql_fetch_array($result)[0];
echo json_encode([$row,($row+9)*27658]);
mysql_close($conn);
?>



