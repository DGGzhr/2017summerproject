<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='malicious_domain';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);

$sql="select *  from  domain";
$result = mysql_query($sql,$conn);

while($row = mysql_fetch_array($result))
{

$arr[] = array(
        'domain' => $row['domain'],
      'country' => $row['country'],
     	'city' => $row['city'],
	'latitude' =>$row['latitude'],
	'longitude' => $row['longitude']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>

