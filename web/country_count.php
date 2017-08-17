<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='time';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);

$sql="select m.country, count(*)as num  from  domain as t  left join  malicious_domain.domain as m on m.domain=t.main where t.time<now() and m.country !='null'  group by m.country order by num  desc limit 0,6";
$result = mysql_query($sql,$conn);

while($row = mysql_fetch_array($result))
{

$arr[] = array(
       
      'country' => $row['country'],
	'count' => $row['num']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>

