
<?php
#$domain="baidu.com";
$domain=$_GET["domain"];
$result=exec("python /home/spark/svm/chaxun.py".' '.$domain);
$string=explode(",",$result);

$arr[]=array(
'domain' => $string[0],
'result' => $string[1],
'time' => $string[2],
'country'=> $string[3],
'city' => $string[4],
'latitude' => $string[5],
'longitude' => $string[6],
'ip1' => $string[7],
'ip2' => $string[8],
'ip3' => $string[9],
'ip4' => $string[10],
);
echo json_encode($arr)
?>
