<?php
	ignore_user_abort();//关掉浏览器，PHP脚本也可以继续执行.
	set_time_limit(0);// 通过set_time_limit(0)可以让程序无限制的执行下去
	$cmd = exec("nohup python Crawler/yun.py ".$_GET['words'] . " " . $_GET['fromdate']. " > python_log.log 2>&1 & ");
	echo "running"
?>