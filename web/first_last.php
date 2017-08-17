<?php
$mysql_server_name='127.0.0.1';

$mysql_username='root';

$mysql_password='123456';

$mysql_database='time';
$conn=mysql_connect($mysql_server_name,$mysql_username,$mysql_password) or die("error connecting") ;
mysql_select_db($mysql_database);
$sql="select a.domain,a.first,a.last,a.ip,a.num,b.country,b.city from 
(select q.domain,q.first,w.last,q.ip,q.num,q.main from (select t.domain, t.time as first,t.ip,b.num,t.main  from (select * from domain where time < now() order by time )as t left join (select domain ,count(*) as num from domain  where time < now() group by domain order by num desc  limit 10) as b on b.domain= t.domain   where t.domain in (select a.domain  from (select domain ,count(*) as num from domain where time < now() group by domain order by num desc  limit 10) as a)   group by t.domain order by b.num desc)as q left join (select t.domain, t.time as last  from (select * from domain where time < now() order by time desc )as t left join (select domain ,count(*) as num from domain where time < now() group by domain order by num desc  limit 10) as b on b.domain= t.domain   where t.domain in (select a.domain  from (select domain ,count(*) as num from domain where time < now() group by domain order by num desc  limit 10) as a)   group by t.domain) as w on w.domain=q.domain ) as a left join (select domain ,country,city from malicious_domain.domain)as b on  a.main=b.domain limit 2,5";
$result = mysql_query($sql,$conn);

while($row = mysql_fetch_array($result))
{

$arr[] = array(
        'domain' => $row['domain'],
        'first' => $row['first'],
	'last'=>$row['last'],
        'ip'=>$row['ip'],
        'country' => $row['country'],
        'city' => $row['city'],
        'num'=>$row['num']
    ); }
echo json_encode($arr);
mysql_close($conn);
?>



