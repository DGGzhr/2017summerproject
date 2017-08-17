<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='malicious_domain';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);

$country=$_GET["country"];
$city=$_GET["city"];
#$city='Beijing';
if ($country == null){
	
$coun = (mysql_query("select country from domain where domain.city = '$city' ",$conn));
$row=mysql_fetch_array($coun);
for($i=0; $row[$i]!= 'None';$i++)
{
	$country=$row[$i];
	break;
	

}
}

$sql="select t.domain,t.time,t.ip,m.country,m.city,m.latitude,m.longitude from time.domain as t left join  malicious_domain.domain as m on t.main=m.domain where m.country ='$country' and t.time < now()   group by t.domain,t.time,t.ip order by time desc ";
$result = mysql_query($sql,$conn);

while($row = mysql_fetch_array($result))
{

$arr[] = array(
        'domain' => $row['domain'],
	'time' => $row['time'],
	'ip'=>$row['ip'],
	'country' => $row['country'],
        'city' => $row['city'],
        'latitude' =>$row['latitude'],
        'longitude' => $row['longitude']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>


