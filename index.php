<html>
	<head>
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
		<script src="http://apps.bdimg.com/libs/jquery.cookie/1.4.1/jquery.cookie.js"></script>
		<style type="text/css">
			body{
				text-align:left;
				margin-left: 250px;
			}
			.s_btn {
				width: 200px;
				height: 34px;
				border: 0;
				color: white;
				letter-spacing: 1px;
				background: #3385ff;
				border-bottom: 1px solid #2d78f4;
				outline: medium;
				-webkit-appearance: none;
				-webkit-border-radius: 0;
				font-size: 14px;
				cursor: pointer;
			}
			.s_ipt {
			    width: 326px;
			    height: 22px;
			    font: 16px/22px arial;
			    margin: 6px 0 0 7px;
			    padding: 0;
			    background: transparent;
			    border: 0;
			    outline: 0;
			    -webkit-appearance: none;
			}
			.from {
			    width: 126px;
			    height: 22px;
			    font: 16px/22px arial;
			    margin: 6px 0 0 7px;
			    padding: 0;
			    background: transparent;
			    border: 0;
			    outline: 0;
			    -webkit-appearance: none;
			}
			.fm {
			    clear: none;
			    margin: 11px 0 0 10px;
			}
			.s_ipt_wr {
			    border: 1px solid #b6b6b6;
			    border-color: #7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;
			    background: #fff;
			    display: inline-block;
			    vertical-align: top;
			    width: 339px;
			    height: 32px;
			    margin-right: 2;
			    border-color: #b8b8b8 #b8b8b8 #ccc #b8b8b8;
			}
			.s_ipt_from {
			    border: 1px solid #b6b6b6;
			    border-color: #7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;
			    background: #fff;
			    display: inline-block;
			    vertical-align: top;
			    width: 139px;
			    height: 32px;
			    margin-right: 10;
			    border-color: #b8b8b8 #b8b8b8 #ccc #b8b8b8;
			}
			.s_msg {
				color: #ff0000;
				font-size: 40;
			}
		</style>

		<script type="text/javascript">
			$(document).ready(function(){
				$("#crawler").click(function(){
					$("#msg").html("正在后台爬.....平均一天需要1s....刷新页面查看结果");
					$.cookie('crawler_words', $("#words").val(), { expires: 365 }); 
					$.cookie('crawler_fromdate', $("#fromdate").val(), { expires: 365 }); 
					htmlobj=$.ajax({url:"crawler.php?words=" + $("#words").val() + 
						"&fromdate=" +
						$("#fromdate").val(),
						async:true,
						success: function(data){
						}});
				});
			});
		</script>
		<script language="JavaScript"> 
			function myrefresh(){ 
				window.location.reload();
			}
			setTimeout('myrefresh()', 30000);
		</script> 
	</head>
	<body>

	
		<br/>
		<br/>
		<br/>

		<span class="s_ipt_from">
			<input name="fromdate" id="fromdate" class="from" value="2017-02-01" maxlength="100" autocomplete="on">
		</span>
		<span class="s_ipt_wr">
			<input name="word" id="words" class="s_ipt" value="YunOS" maxlength="100" autocomplete="on">
			
		</span>
		<span>
		<button id="crawler" class="s_btn">爬一下百度新闻</button>
		<a href="http://pudding.ie8384.com/pudding/">跳转到 Google News</a>
		</span>
		
	
		<br/>
		<br/>
<br/>

		1、起始时间格式为yyyy-mm-dd，如：2016-02-03<br/>
		2、多个关键词以空格隔开
		3、爬一天的新闻大概需要1s
		<br/>
		<br/>
		<br/>
		<p id="msg" class="s_msg">如果点击后还没有结果，请稍后再刷新</p>
		<br/>
		<br/>
		<br/>
		<?php

		function dir_list($dir){
			$dh = opendir($dir);             
     		$return = array();
      		$i = 0;
          	while($file = readdir($dh)){    
             	if($file!='.' and $file!='..' && strstr($file, ".xls")){
              		$path = $dir.'/'.$file;          
              		$filetime[] = date("Y-m-d H:i:s",filemtime($path));   
   
              		$return[] =  $file;
          		}
          	}  
          	closedir($dh);             
          	array_multisort($filetime,SORT_DESC,SORT_STRING, $return);//按时间排序
          	return $return;               
     	}
		echo "历史文件列表:<br/>";
		$current_dir = 'output';
		$currentTime = date('Y-m-d H:i:s',time());
		if(is_dir($current_dir)) {
			$files = dir_list($current_dir);
			$num = count($files); 
			for($i=0; $i<$num; ++$i){ 
				$url='http://'.$_SERVER['HTTP_HOST'].$_SERVER["REQUEST_URI"];
				
				echo "<a href='".$url."/".$current_dir."/$files[$i]'>$files[$i]</a>";
				$ctime = filectime($current_dir."/".$files[$i]);
				$createdTime = date("Y-m-d H:i:s",$ctime);
				$date=floor((strtotime($currentTime)-strtotime($createdTime))/86400);
				if ($date > 0) {
					echo "        Created:".$createdTime;
				}else {
					echo "        Created:";
					$currentTime_time = strtotime($currentTime);
					$createdTime_time = strtotime($createdTime);

					$tmp = ($currentTime_time-$createdTime_time)%86400;
					$hour=floor($tmp/3600);
					if ($hour > 0) {
						echo $hour."小时";
					}
					$tmp = $tmp%3600;
					$minute=floor($tmp/60);
					if ($minute > 0) {
						echo $minute."分钟";
					}
					$tmp = $tmp%60;
					$second=floor($tmp);
					echo $second."秒以前";
				}
				echo "<br/>";
			}
		}
		?>

		<script language="JavaScript"> 
			if ($.cookie('crawler_words') != null) {
				$("#words").val($.cookie('crawler_words'));
				$("#fromdate").val($.cookie('crawler_fromdate'));
			}
		</script> 
	</body>
</html>