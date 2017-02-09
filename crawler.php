<?php
	echo "python Crawler/yun.py ".$_GET['words'];
	$cmd = exec("python Crawler/yun.py ".$_GET['words'] . " 2>&1",$ret);
	print_r($ret);
?>