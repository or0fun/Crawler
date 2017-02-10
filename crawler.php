<?php
	echo "python Crawler/yun.py ".$_GET['words']." ".$_GET['fromdate'];
	$cmd = exec("python Crawler/yun.py ".$_GET['words'] . " " . $_GET['fromdate'] . " 2>&1",$ret);
	print_r($ret);
?>