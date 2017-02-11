<?php
	$cmd = exec("nohup python Crawler/yun.py ".$_GET['words'] . " " . $_GET['fromdate'] . " 2>&1 |tee python_error.log > python_log.log &");
	echo "running"
?>