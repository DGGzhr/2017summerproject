<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='time';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);


$time1=$_GET["time1"];
$time2=$_GET["time2"];
$date1=$time1." ".$time2;
$date2=date('Y-m-d H:i:s',strtotime("$date1+6 hour"));
$sql="select t.domain,t.time,t.ip,m.country,m.city from time.domain as t left join  malicious_domain.domain as m on t.main=m.domain   where t.time > '$date1' and t.time < '$date2' order by t.time";
$result = mysql_query($sql,$conn);
while($row = mysql_fetch_array($result))
{
$arr[] = array(
        'domain' => $row['domain'],
        'date' => $row['time'],
        'ip' => $row['ip'],
	'country' => $row['country'],
	'city' => $row['city']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>

