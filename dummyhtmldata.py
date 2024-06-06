html="""
<!DOCTYPE html>
<html class="ap__fonts" lang="en-IN">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta content='width=device-width, initial-scale=1.0, maximum-scale=5.0' name='viewport' />

	<!-- Meta -->
	<meta name="theme-color" content="#0091FF">
	<meta name="apple-mobile-web-app-status-bar-style" content="#0091FF">
			<title>Bugasura: Everyone&#039;s Testing Assistant</title>
				<link rel="canonical" href="https://my.bugasura.io/apps" />
	<meta name="author" content="AppAchhi Technologies">
	
				
		
		<link rel="icon" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/bugasura-favicon.png">
		<!-- <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script> -->

		<!-- CSS -->
		<link media="all" rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/material.min.css">
				<link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/bootstrap-tagsinput.css">
		<link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/toaster/toastr.min.css">
		<link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/stylesheets/bootstrap.min.css">
									<link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/pages/login.css">
																														<link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/stylesheets/style-clean.css">
												<link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/platformCustom2.css">
																																					<link rel="preload" as="style" onload="this.rel='stylesheet'" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/cropper.min.css">
									<!-- <link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/multi-select.dev.css">
			<link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/multi-select.dist.css"> -->
			<!-- <link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/gridster.min.css">
			<link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/lobipanel.css"> -->
			<!-- <link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/animate.min.css"> -->
									<!-- <link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/stylesheets/icon.css"> -->
							<link rel="stylesheet" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/introjs.css">
				<link rel="stylesheet" type="text/css" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/pages/appsLandingPage.css" />
<link rel="stylesheet" type="text/css" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/pages/answersPage.css" />
<link rel="stylesheet" type="text/css" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/pages/pageList.css" />
<link rel="stylesheet" type="text/css" href="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/css/pages/releaseNotes.css" />
		<!-- SCRIPTS -->
				<!-- Microsoft clarity -->
		<script type="text/javascript">
			(function(c,l,a,r,i,t,y){
				c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
				t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
				y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
			})(window, document, "clarity", "script", "gqbmgleud6");
		</script>
				<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/jquery.min.js"></script>
				<script defer type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/lazyload.js"></script>
																		<!-- <script>(function(c,a){if(!a.__SV){var b=window;try{var d,m,j,k=b.location,f=k.hash;d=function(a,b){return(m=a.match(RegExp(b+"=([^&]*)")))?m[1]:null};f&&d(f,"state")&&(j=JSON.parse(decodeURIComponent(d(f,"state"))),"mpeditor"===j.action&&(b.sessionStorage.setItem("_mpcehash",f),history.replaceState(j.desiredHash||"",c.title,k.pathname+k.search)))}catch(n){}var l,h;window.mixpanel=a;a._i=[];a.init=function(b,d,g){function c(b,i){var a=i.split(".");2==a.length&&(b=b[a[0]],i=a[1]);b[i]=function(){b.push([i].concat(Array.prototype.slice.call(arguments,
0)))}}var e=a;"undefined"!==typeof g?e=a[g]=[]:g="mixpanel";e.people=e.people||[];e.toString=function(b){var a="mixpanel";"mixpanel"!==g&&(a+="."+g);b||(a+=" (stub)");return a};e.people.toString=function(){return e.toString(1)+".people (stub)"};l="disable time_event track track_pageview track_links track_forms track_with_groups add_group set_group remove_group register register_once alias unregister identify name_tag set_config reset opt_in_tracking opt_out_tracking has_opted_in_tracking has_opted_out_tracking clear_opt_in_out_tracking people.set people.set_once people.unset people.increment people.append people.union people.track_charge people.clear_charges people.delete_user people.remove".split(" ");
for(h=0;h<l.length;h++)c(e,l[h]);var f="set set_once union unset remove delete".split(" ");e.get_group=function(){function a(c){b[c]=function(){call2_args=arguments;call2=[c].concat(Array.prototype.slice.call(call2_args,0));e.push([d,call2])}}for(var b={},d=["get_group"].concat(Array.prototype.slice.call(arguments,0)),c=0;c<f.length;c++)a(f[c]);return b};a._i.push([b,d,g])};a.__SV=1.2;b=c.createElement("script");b.type="text/javascript";b.async=!0;b.src="undefined"!==typeof MIXPANEL_CUSTOM_LIB_URL?
MIXPANEL_CUSTOM_LIB_URL:"file:"===c.location.protocol&&"//cdn4.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//)?"https://cdn4.mxpnl.com/libs/mixpanel-2-latest.min.js":"//cdn4.mxpnl.com/libs/mixpanel-2-latest.min.js";d=c.getElementsByTagName("script")[0];d.parentNode.insertBefore(b,d)}})(document,window.mixpanel||[]);
mixpanel.init("6abad1f7e2d0734c336c857e46acab45", {batch_requests: true})</script> -->


	</head>


	<!-- BODY -->
	<body class="show-content getApps   ap__navigation--new leftnav-visible">

					<div class="leftnav-menu-wrapper"></div>
		
		<div> <!--  id="loading_cubes" -->
			<div class="yc-cube-grid hidden" id="loading">
				<div class="yc-cube yc-cube1"></div>
				<div class="yc-cube yc-cube2"></div>
				<div class="yc-cube yc-cube3"></div>
				<div class="yc-cube yc-cube4"></div>
				<div class="yc-cube yc-cube5"></div>
				<div class="yc-cube yc-cube6"></div>
				<div class="yc-cube yc-cube7"></div>
				<div class="yc-cube yc-cube8"></div>
				<div class="yc-cube yc-cube9"></div>
			</div>
						<div class="random-message hidden"> Tip: Open any block in coverage report to access Memory, CPU and Network results </div>
		</div>
		<div >
												<nav class="ap__siderbar-compact navbar-fixed-top hidden-xs">
	<ul class="nav nav-stacked">
		<li class="leftnav-toggle hidden leftnav-toggle--arrow">
			<span class="material-icons">&#xe5cb</span>
		</li>
		<li class="logo-section text-center">
			<a href="https://my.bugasura.io/apps">
				<img width="35px" height="35px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/platform-plan/white/logo_white.svg" alt="Logo">
			</a>
		</li>
					<li class="active text-center">
				<a href="https://my.bugasura.io/apps" class="project-btn">
					<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/project_page_icon_white.svg" alt="Home">
					<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/project_page_icon.svg" alt="Home">
				</a>
				<div class="custom-tooltip">
					<p class="title">Projects</p>
				</div>
			</li>
							<li class="text-center">
					<a href="https://my.bugasura.io/dashboard/user" class="my-dashboard-btn">
						<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/dashboard.svg" alt="Dashboard">
						<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/dashboard_coloured.svg" alt="Dashboard">
					</a>
					<div class="custom-tooltip">
						<p class="title">Dashboard</p>
					</div>
				</li>
			
			<li class="gap text-center hidden">
				<a href="#" rel="nofollow">
					<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/notification.svg" alt="Notifications">
					<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/notification_coloured.svg" alt="Notifications">
					<span class="ap__siderbar-compact-dot"></span>
				</a>
				<div class="custom-tooltip">
					<p class="title">Notifications</p>
				</div>
			</li>
											<li class="gap text-center">
					<a href="javascript:void(0);" id="whats_new" rel="nofollow">
						<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/gift.svg" alt="What's New">
						<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/gift_coloured.svg" alt="What's New">
													<span class="ap__siderbar-compact-dot"></span>
											</a>
					<div class="custom-tooltip">
						<p class="title">What's New</p>
					</div>
				</li>
			
			<li class=" text-center ">
				<a href="https://my.bugasura.io/teams/manage" class="leftnav-settings-btn">
					<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/setting.svg" alt="Manage">
					<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/setting_coloured.svg" alt="Manage">
				</a>
				<div class="custom-tooltip">
					<p class="title">Manage</p>
				</div>
			</li>
							<li class="text-center">
					<a href="javascript:void(0);" rel="nofollow" id="intro_help"  class="leftnav-tour-restart">
						<img loading="lazy" width="22px" height="22px" class="icon icon--white" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/help.svg" alt="Tour">
						<img loading="lazy" width="22px" height="22px" class="icon icon--coloured" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/help_coloured.svg" alt="Tour">
					</a>
					<div class="custom-tooltip">
						<p class="title">Restart Tour</p>
					</div>
				</li>
							<!-- User Info and Login -->
		<li class="text-center">
							<a href="https://my.bugasura.io/account/userprofile" class="leftnav-user-profile">
					<div class="js-update-user-avatar">
													<div class="up__avatar-icon-holder header-avatar">
								<img class="icon up__avatar-icon"
									src="https://s3-ap-south-1.amazonaws.com/uploads.v2.appachhi.com/userProfileImages/70292.1717149313.avatar-15.svg" alt="Avatar">
							</div>
											</div>
				</a>
				<div class="holder">
					<div class="custom-tooltip custom-tooltip--avatar">
						<div class="text-center">
							<div class="box js-update-user-avatar">
																	<div class="up__avatar-icon-holder header-avatar">
										<img class="icon up__avatar-icon"
											src="https://s3-ap-south-1.amazonaws.com/uploads.v2.appachhi.com/userProfileImages/70292.1717149313.avatar-15.svg" alt="Avatar">
									</div>
															</div>
							<p class="up__name hidden-xs js-up-update-user-name handel-over-flow">Piyush Waghmare</p>
							<span class="ap__header-profile--name ap__header-profile--eamil text-center">piyushwaghmarehere@gmail.com</span>
							<a href="https://my.bugasura.io/upgradePlan" class="user-profile-upgrade-link hidden-xs">
																																																	<p class="up__plan" data-plan="free" data-bg="true">
									<span class="ap__text">Free Plan</span>																											</p>
							</a>
							<a href="https://my.bugasura.io/Account/logout" class="side-navbar-logout">
								<div class="logout-section">
									<img class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/icons/log_out_red.svg" alt="">
									<span>Logout</span>
								</div>
							</a>
						</div>
					</div>
				</div>
					</li>
	</ul>
</nav>

													<!-- Navigation Bar -->
	<div class="app__header--info affix visible-xs">
	<div class="header-div test-plan-cards-area ap__header--new">
		<nav class="navbar navbar-default navbar-fixed-top">
			<div class="container-fluid logo-container">
								<a href="https://my.bugasura.io/apps" class="navbar-brand new__app_header_nav">
					<img loading="lazy" class="js-logo logo-bugasura-new.png__logo-bugasura-new.png hidden-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/platform-plan/logo-bugasura-new.png" alt="Bugasura">
					<img loading="lazy" width="120px" height="30px" class="js-logo logo-bugasura-new.png__logo-bugasura-new.png visible-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/platform-plan/white/logo-bugasura-new.png" alt="Bugasura">
				</a>
									<ul class="nav navbar-nav top-nav hidden-xs">
						<a href="https://my.bugasura.io/apps"
							class="ap__header-nav active ">
							Projects
						</a>
						<a href="https://my.bugasura.io/dashboard/user"
							class="ap__header-nav ">
							My Dashboard
						</a>
											</ul>
								<div class="product-list">
											<div class="visible-xs">
							<button class="header-project-search" type="button">
								<img class="settings-icon-mobile visible-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/search-white.svg" alt="Settings">
							</button>
						</div>
						<div class="visible-xs">
							<button class="js-project-filter" type="button">
								<img class="settings-icon-mobile visible-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/filter-white.svg" alt="Settings">
							</button>
						</div>
						<div class="dropdown settings-menu hidden">
							<button class="btn setting-btn dropdown-toggle" id="settings_menu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" type="button" name="settings-menu-btn">
								<img class="settings-icon hidden-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/gear_blueblack.svg" alt="Settings">
								<img class="settings-icon-hovered hidden-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/gear_blue.svg" alt="Settings">
								<img class="settings-icon-mobile visible-xs" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/gear_white.svg" alt="Settings">
								<p class="hidden-xs">Manage</p>
								<span class="material-icons hidden-xs">expand_more</span>
							</button>
							<ul class="dropdown-menu" aria-expanded="false" aria-labelledby="settings_menu">
								<li>
									<a href="https://my.bugasura.io/teams/manage" title="Teams">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/teams_black.svg" alt="Teams">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/teams_blue.svg" alt="Teams">
										Teams
									</a>
								</li>
								<li class="js_teams_links ">
									<a href="https://my.bugasura.io/issueStatus/manage" title="Workflows">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/workflows_black.svg" alt="Workflows">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/workflows_blue.svg" alt="Workflows">
										Workflows
									</a>
								</li>
																<li class="hidden">
									<a href="#" id="slack_btn_click" title="Slack Connect">
										<img class="settings-menus-icon visible" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/slack.svg" alt="Slack">
										Slack Connect
									</a>
								</li>
								<li>
									<a href="https://my.bugasura.io/notifications" title="Notifications">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/integration_black.svg" alt="Moderate Comments">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/integration_blue.svg" alt="Moderate Comments">
										Notifications
									</a>
								</li>
								<li class="hidden">
									<a href="https://my.bugasura.io/teamIntegration" title="Team Integrations">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/integration_black.svg" alt="Moderate Comments">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/team_integration_blue.svg" alt="Moderate Comments">
										Team Integrations
									</a>
								</li>
							</ul>
						</div>
										<div class="dropdown user-profile hidden">
													<button class="btn user-profile-btn dropdown-toggle" id="user_profile" data-toggle="dropdown" aria-haspopup="true"
								aria-expanded="false" type="button" name="button">
																	<div class="up__avatar-icon-holder header-avatar">
										<img class="icon up__avatar-icon"
											src="https://s3-ap-south-1.amazonaws.com/uploads.v2.appachhi.com/userProfileImages/70292.1717149313.avatar-15.svg" alt="Avatar">
									</div>
																<div class="name">
									<span class="ap__header-profile--name hidden-xs">Piyush Waghmare</span>
									<span class="ap__header-profile--name ap__header-profile--eamil hidden-xs">piyushwaghmarehere@gmail.com</span>
								</div>
								<span class="material-icons hidden-xs">&#xe5cf</span>
							</button>
							<ul class="dropdown-menu" aria-expanded="false" aria-labelledby="user_profile">
								<div class="user-dets-container">
									<span class="ap__header-profile--name">Piyush Waghmare</span>
									<span class="ap__header-profile--name ap__header-profile--eamil">piyushwaghmarehere@gmail.com</span>
									<a href="https://my.bugasura.io/upgradePlan" class="user-profile-upgrade-link" ><p class="up__plan up__plan--header" data-plan="free">Free Plan</p> </a>
								</div>
								<li>
									<a href="https://my.bugasura.io/account/userprofile" title="User Profile" class="logout u-dis-f-rc">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/user_profile.svg" alt="User profile">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/user_profile_blue.svg" alt="User profile">
										User Profile
									</a>
								</li>
								<li>
									<a href="https://my.bugasura.io/manageSubscription" title="Subscription" class="logout u-dis-f-rc">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/subscription.svg" alt="Subscription">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/subscription_blue.svg" alt="Subscription">
										Subscription
									</a>
								</li>
								<li>
									<a href="https://my.bugasura.io/Account/logout" title="Logout" class="logout">
										<img class="settings-menus-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/logout_black.svg" alt="Logout Icon">
										<img class="settings-menus-icon-hovered" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/logout_blue.svg" alt="Logout Icon">
										Logout
									</a>
								</li>
							</ul>
											</div>
				</div>
			</div>
			<div class="search-bar hidden">
				<div class="search-bar-content">
					<div class="input-group testcase__search bug-report__search answer__search mobile">
						<span class="input-group-addon" id="basic-addon7"><img src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/search-white.svg" alt="Back"></span>
						<input class="form-control js-input-search" data-toggle="search" type="text" placeholder="  Search" aria-describedby="basic-addon7" autocomplete="off">
						<div class="testcase_serach--close projects-header-search--close js-close">
							<img src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/primary-nav/close-white.svg" alt="Back">
						</div>
					</div>
				</div>
			</div>
		</nav>
	</div>
</div>
<script type="text/javascript">
	$(document).ready(function () {

		// Close subscription expiry banner
		$('#close-subs-banner').on('click',function () {
			$('#subscription_banner_container').remove();
		});

		$('.header-project-search').on('click',function () {
			$('.navbar .search-bar').removeClass('hidden');
			$('.js-input-search').val('');
			$('.form-control').focus();
		});

		$('.js-project-filter').on('click',function () {
			if($('.js-project-filter').hasClass('active')){
				$('.js-project-filter').removeClass('active');
				$('.project-filters-mobile').addClass('hidden').removeClass('open');
				$('.dashboard-tab-options').removeClass('filter-active');
			} else {
				$('.js-project-filter').addClass('active');
				$('.project-filters-mobile').removeClass('hidden').addClass('open');
				$('.dashboard-tab-options').addClass('filter-active');
			}
		});

		$('#slack_btn_click, .slack_btn_click').on('click',function (e) {
			e.preventDefault();
			isSlackEnabled();
		});

		/************************************************************/
		/*	This fuction check whether slack integration is enabled.	*/
		/************************************************************/
		function isSlackEnabled () {
			$.post('https://my.bugasura.io/slack/getUserSlack',{
					slack 	: 'is_slack_enabled'
				},isSlackEnabledCallback,'json');
		}

		// Callback func to isJiraEnabled
		function isSlackEnabledCallback ( response ) {
			if ( response.status == 'OK' ) {
				if ( response.slackAppInstallUrl ){
					window.open(response.slackAppInstallUrl);
				}
			} else {
				// In case of error response show message
				toastr.error(response.message);
				if ( response.isExpired ){
					window.location.href='https://my.bugasura.io/upgradePlan';
				}
			}
		}


		if ($(window).width() <= 736) {
			$("#test_plan_link_list").insertAfter($("#test_plan_link"));
		}

		$(".header-team__name").on('click',function (e) {
			if ( $(".team-list-section").hasClass("open") )
				return ;
			setTimeout( () => $("#currentTeam").click(), 100 )
		});

		$(document).on('click', '.sinup-link', function (e) {
			e.preventDefault();
			// Reset the form fields/validation error messages for each
			resetForms();    // function is present in the signUp.volt file
			$('#LoginModal').modal('show');
		});

		$('.user-profile .user-profile-btn .handel-over-flow').tooltip({ container: $(this).attr('data-container') });

		setTimeout(function () {
			if (localStorage.getItem("selected_platform") !== null && localStorage.getItem("selected_platform").length !== 0) {
				//$(".product-list a[data-product='Apps']").click();
				$(".product-list a[data-product=" + "'" + localStorage.getItem("selected_platform") + "'" + "]").click();
			} else {
				$(".product-list a[data-product='Android']").click();
			}
		}, 10);
	});

	function iTrim(str, char) {
		var replace = "\^\\" + char + "+|\\" + char + "+$";
		var re = new RegExp(replace, "g");
		return str.replace(re, "");
	}

</script>

										<!-- Load the content first -->
			<div id="main-content">
				<div id="center-content">
	<div class="area ap__apps-page--new">
	<div class="area-content-dashboard">
		
			<div class="projectlist-banner ap__inner-section container-fluid bc ap__inner-section--art bc hidden-xs">
				<div id="project_banner" class="">
					<div class="ap__inner-art">
						<div class="container-fluid">
							<div class="row row-flex projectlist-banner-img">
								<img loading="lazy" width="1095px" height="246px" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/banner_projectlist.svg" alt="Abstract" class="img-responsive" >
							</div>
						</div>
					</div>
					<div class="title-section">
						<div class="banner-header ap__inner-section--details" >
							<div class="banner-text-dash"></div>
							<p class="banner-title-name ap__inner-section--art">Projects</p>
						</div>
						<h1 class="banner-title ap__inner-section--title">Multi tasking is hard. Focus is good.</h1>
						<p class="dashboard-banner-tagline ap__inner-section--details">Name your projects the way your teams recognize it.</p>

						<div class="banner-header ap__inner-section--details" >
							<div class="dropdown hidden-xs ">
							</div>
							<img loading="lazy" width="18px" height="19x" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/dashboard_banner_img.svg" alt="Abstract" class="img-responsive dashboard-banner-img hidden" >
						</div>
					</div>
				</div>
								<div class="u-dis-f-rc dashboard-tab-options">
					<div id="my_projects" class="project-tab-js" data-project-tab="my_project"  data-project-type="">
						<img loading="lazy" width="12px" height="12px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_favourite_project_dark_blue_icon.svg" alt="My Favourites">
						<img loading="lazy" width="16px" height="16px" class="icon-active" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_favourite_project_icon.svg" alt="My Favourites">
						<span class="project-type-label">My Favourites</span>
						<span class="project-count">(<span class="count">0</span>)</span>
					</div>
					<div class="tab__separator"></div>
					<div id="all_projects" class="project-tab-js" data-project-tab="all" data-project-type="all">
						<img loading="lazy" width="12px" height="12px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/all_project_dark_blue_icon.svg" alt="All">
						<img loading="lazy" width="16px" height="16px" class="icon-active" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/all_project_icon.svg" alt="All">
						<span class="project-type-label">All</span>
						<span class="project-count">(<span class="count">2</span>)</span>
					</div>
					<div id="team_projects" class="project-tab-js" data-project-tab="my_team" data-project-type="">
						<img loading="lazy" width="12px" height="12px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_team_project_dark_blue_icon.svg" alt="My Team Projects">
						<img loading="lazy" width="16px" height="16px" class="icon-active" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_team_project_icon.svg" alt="My Team Projects">
						<span class="project-type-label">Team Projects</span>
						<span class="project-count">(<span class="count">1</span>)</span>
					</div>
					<div id="contributed_projects" class="project-tab-js" data-project-tab="contributed" data-project-type="contributed">
						<img loading="lazy" width="12px" height="12px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_following_project_dark_blue_icon.svg" alt="Following">
						<img loading="lazy" width="16px" height="16px" class="icon-active" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_following_project_icon.svg" alt="Following">
						<span class="project-type-label">Following</span>
						<span class="project-count">(<span class="count">1</span>)</span>
					</div>

				</div>
			</div>
			<div class="">
																															<div class="recent-apps-dashboard--bg container-fluid visible-xs">
				<div class="row content">
					<div class="col-xs-12 ap__welcom-msg animated fadeIn">
						<h1 class="recent-apps-dashboard__text--primary">Projects
						</h1>
						<p class="recent-apps-dashboard__text--tertiary">
							You can name your project after your app to start with.
						</p>
					</div>
				</div>
			</div>
						</div>
			<div id="apps_tab_container" class="">
															<div class="recent-apps-dashboard__content">
					<div class="selected-tab-heading" > <h2>  Team Projects  </h2> </div>
				<div class="row answer__tools">
						<div class="col-xs-12 padding-zero hidden-xs">
				<div class="dashboard-dropdown-options">
					<div class="u-dis-f-rc u-dis-flex-1 dropdown-list mobile">
												<div class="input-group testcase__search bug-report__search answer__search hidden-xs">
							<span class="input-group-addon"><img src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/search_back_icon.svg" alt="Back"></span>
							<input class="form-control js-input-search" data-toggle="search" type="text" placeholder="Search" aria-describedby="basic-addon1" autocomplete="off">
							<div class="js-testcase_serach--close testcase_serach--close close projects-search--close" style="display: none;">
								<i class="material-icons">close</i>
							</div>
						</div>
						<div class="filter-project-options issue-list-sort-filter js-bug-filter-types">
							<div class="dropdown bug-update__dropdown bug-report__filter">
								<button type="button" class="mdl-button mdl-js-button mdl-js-ripple-effect bug-report__filter--button bug-report__all dropdown-toggle"
									id="project_filter_button">
									<img class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons8-issue-filter.svg" alt="Filter">
									<img class="icon-blue" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons8-issue-filter-blue.svg" style="display: none;" alt="Filter">
									<span class="main">Filter</span>
									<span class="colon hidden">&nbsp;:&nbsp;</span>
									<span class="filter-text hidden"></span>
									<span class="material-icons">&#xe313</span>
								</button>
								<ul class="dropdown-menu ap__dropdown--menu bug-filter-dropdown-menu new">
																			<li class="dropdown-submenu js-bug-types">
											<button type="button" class="mdl-button mdl-js-button mdl-js-ripple-effect bug-report__all dropdown-toggle bug-filter-btns" data-toggle="dropdown">
												<img class="br-btn-images" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/teams_filter.svg" alt="Teams"> Teams <span class="material-icons">keyboard_arrow_right</span>
											</button>
											<ul class="dropdown-menu ap__dropdown--menu new" data-list="assignees">
												<li class="input">
													<input type="text" id="teams_filter_search_input" class="form-control js-search-list"  placeholder="Search teams"
														data-do="search" data-target="#teams_filter">
													<i class="material-icons js-search-list-close" style="display: none;">close</i>
												</li>
												<div id="teams_filter" class="scroll scroll-thin">
																																																								<li class="">
																<a href="javascript:void(0);"
																	id="tm_79745" title="DZ"
																	data-column="teams" data-value="79745"
																	data-text-value="DZ">
																	<span class="custom-filter-checkbox">
																		<i class="material-icons selected-filter-item-check">&#xe876</i>
																	</span>
																	<span class="text ap__text">DZ</span>
																</a>
															</li>
																																																								<li class="">
																<a href="javascript:void(0);"
																	id="tm_43608" title="Bugasura Team"
																	data-column="teams" data-value="43608"
																	data-text-value="Bugasura Team">
																	<span class="custom-filter-checkbox">
																		<i class="material-icons selected-filter-item-check">&#xe876</i>
																	</span>
																	<span class="text ap__text">Bugasura Team</span>
																</a>
															</li>
																										<li class="no-results hidden">
														<a href="#" rel="nofollow">Ah! That ain't here.</a>
													</li>
												</div>
											</ul>
										</li>
																		<li class="dropdown-submenu js-bug-types">
										<button type="button" class="mdl-button mdl-js-button mdl-js-ripple-effect bug-report__all dropdown-toggle bug-filter-btns" data-toggle="dropdown">
											<img class="br-btn-images" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/platform_filter.svg" alt="Platform">
											Platform
											<span class="material-icons">keyboard_arrow_right</span>
										</button>
										<ul class="dropdown-menu ap__dropdown--menu new">
											<div id="platform_filter" class="scroll scroll-thin">
												<li>
													<a id="tab_index_1" href="javascript:void(0);" data-column="platform" data-value="AndroidApps" data-text-value="Android" class="mdl-button mdl-js-button mdl-js-ripple-effect ext-capitalize app-category-tab--js">
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">Android</span>
													</a>
												</li>
												<li>
													<a id="tab_index_2" class="mdl-button mdl-js-button mdl-js-ripple-effect app-category-tab--js" href="javascript:void(0);" data-column="platform" data-value="iOSApps" data-text-value="iOS">
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">iOS</span>
													</a>
												</li>
												<li>
													<a id="tab_index_3" class="mdl-button mdl-js-button mdl-js-ripple-effect app-category-tab--js" href="javascript:void(0);" data-column="platform" data-value="AndroidMobileweb" data-text-value="Android Mobile Web" >
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">Android Mobile Web</span>
													</a>
												</li>
												<li>
													<a id="tab_index_4" class="mdl-button mdl-js-button mdl-js-ripple-effect app-category-tab--js" href="javascript:void(0);" data-column="platform" data-value="iOSMobileweb" data-text-value="iOS Mobile Web">
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">iOS Mobile Web</span>
													</a>
												</li>
												<li>
													<a id="tab_index_5" class="mdl-button mdl-js-button mdl-js-ripple-effect app-category-tab--js" href="javascript:void(0);" data-column="platform" data-value="DesktopWeb" data-text-value="Desktop Web">
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">Desktop Web</span>
													</a>
												</li>
												<li>
													<a id="tab_index_6" class="mdl-button mdl-js-button mdl-js-ripple-effect app-category-tab--js" href="javascript:void(0);" data-column="platform" data-value="MultipleMultiple" data-text-value="Multi Platform">
														<span class="custom-filter-checkbox">
															<i class="material-icons selected-filter-item-check">&#xe876</i>
														</span>
														<span class="text ap__text">Multi Platform</span>
													</a>
												</li>
											</div>
										</ul>
									</li>
									<li class="dropdown-submenu js-bug-types">
										<button type="button" class="mdl-button mdl-js-button mdl-js-ripple-effect bug-report__all dropdown-toggle bug-filter-btns" data-toggle="dropdown">
											<img class="br-btn-images" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/type_filter.svg" alt="Type">
											Type
											<span class="material-icons">keyboard_arrow_right</span>
										</button>
										<ul class="dropdown-menu ap__dropdown--menu new">
											<div id="type_filter" class="scroll scroll-thin">
												<li title="public">
													<a id="public" class="project-types-js team-list-item mdl-button mdl-js-button mdl-js-ripple-effect" href="javascript:void(0);" data-project-type="public" data-column="type" data-value="public" data-text-value="Public">
														<input type="radio" id="type_public" class="" name="types" value="1">
														<span class="text ap__text">Public</span>
													</a>
												</li>
												<li title="private">
													<a id="private" class="project-types-js team-list-item mdl-button mdl-js-button mdl-js-ripple-effect" href="javascript:void(0);" data-project-type="private" data-column="type" data-value="private" data-text-value="Private">
														<input type="radio" id="type_private" class="" name="types" value="1" >
														<span class="text ap__text">Private</span>
													</a>
												</li>
											</div>
										</ul>
									</li>
									<li class="dropdown-submenu js-bug-types">
										<button type="button" class="mdl-button mdl-js-button mdl-js-ripple-effect bug-report__all dropdown-toggle bug-filter-btns" data-toggle="dropdown">
											<img class="br-btn-images" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/status_filter.svg" alt="Status">
											Status
											<span class="material-icons">keyboard_arrow_right</span>
										</button>
										<ul class="dropdown-menu ap__dropdown--menu new">
											<div id="status_filter" class="scroll">
												<li title="All">
													<a id="all" class="js-project-status mdl-button mdl-js-button mdl-js-ripple-effect" href="javascript:void(0);" data-column="status" data-value="all" data-text-value="All">
														<input type="radio" id="status_all" class="" name="status" value="1" >
														<span class="text ap__text">All</span>
													</a>
												</li>
												<li title="Archive">
													<a id="archive" class="js-project-status mdl-button mdl-js-button mdl-js-ripple-effect" href="javascript:void(0);" data-text-value="Archive" data-column="status" data-value="archive">
														<input type="radio" id="status_archived" class="" name="status" value="1" >
														<span class="text ap__text">Archive</span>
													</a>
												</li>
											</div>
										</ul>
									</li>
								</ul>
							</div>
						</div>
											</div>
					<button id="create_project" class="banner_btn mdl-button mdl-js-button	mdl-js-ripple-effect  js-create_project create-functional-report ap__btn ap__btn--new ap__btn--primary ap__btn--primary-new ">
							+ Create Project
					</button>
				</div>
				<div class="apps_shown-count visible-hidden">
					<span class="apps-item-count">Showing <span id="apps_shown_count"></span> of <span id="apps_total_count"></span>
				</div>
			</div>
					</div>
		<span id="bug_report_multi_search" class="hidden">
			<ul class="list-inline u-dis-flex-1 js__filter-tags">
				<li class="text hidden-xs"><span class="search_results_count">1</span>&nbsp;
					<span class="ap__text">Results</span>
				</li>
								<li class="filter-dets line">
					<button id="clear_issue_filters" class="btn btn-primary">Clear Filters</button>
				</li>
							</ul>
					</span>
		<div id="platform_tab_container">
				<div class="answer-dashboard tab-content" data-team-id="allTeams">
				<!-- No Apps available -->
				<!-- List the all types of apps -->
				<div class="answer__reports tab-pane active" id="all_apps">
					<div class="answer__reports-no-apps" hidden>
						<img loading="lazy" width="366px" height="230px" class="img" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/empty-illustrations/no-issues-found.gif" alt="No results">
						<div class="js-no-apps"> <span class="heading">No Project Found</span></div>
					</div>
					<div class="col-md-3 col-sm-6 col-xs-12 new-create-block" hidden>
						<div data-platform = "Android" data-platformType = "Apps" class="row create-new-report-block">
							<div class="row">
								<img loading="lazy" width="400px" height="277px" class="ap__project--img" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/empty-illustrations/create_new_project.gif" alt="Create Project">
								<span class="text">No project in that category has been created yet. <br> Time to do?</span>
							</div>
						</div>
					</div>
																																																															<div class="apps_block__js " data-app_id="107318">
							<div class="row new-grid-card ">
								<div class="col-xs-12 select-box" data-report-list-url="https://my.bugasura.io/issues/107318">
																																																								<div class="dropdown ">
																					<button class="mdl-button mdl-js-button mdl-button--icon ap__inner-section--btn js-app-favourite_add_remove  app-favourite_add_remove js-my-project-add-remove  ap__project-favourite_remove" title="Add this project to my favourites" " 												data-favourite_project="0"  title="Add this project to my favourites" data-toggle="tooltip"
												data-placement="top" data-app_id="107318" data-app_name="101" data-team_id="79745">
												<img loading="lazy" width="85px" height="150px" class="favourite_project_icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/favourite_project.svg" alt="Favourite Project">
												<img loading="lazy" width="85px" height="150px" class="favourite_project_icon favourite_project__remove" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_favourite_project_remove.svg" alt="Pin Project">
											</button>
																															<button class="js-project_pin-unpin mdl-button mdl-js-button mdl-button--icon ap__inner-section--btn app-pin_unpin ap__project-unpin" title="Pin" data-toggle="tooltip" data-placement="top"  data-app_id="107318" data-team_id="79745">
												<img loading="lazy" width="85px" height="150px" class="project__pin_icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/pin_vertical.svg" alt="Pin Project">
																								<img loading="lazy" width="85px" height="150px" class="project__pin_icon project__unpin" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/unpin_vertical.svg" alt="Pin Project">
											</button>
																				<button id="app_dropdown-107318_all"
											class="mdl-button mdl-js-button mdl-button--icon ap__inner-section--btn app-page-menu " data-toggle="dropdown">
											<i class="material-icons">&#xe5d4</i>
										</button>
										<ul class="dropdown-menu ap__dropdown--menu app_options-dropdown" for="app_dropdown-107318_all">
											<li class="project-menu visible-xs">
												<a>
													<span>Project Menu</span>
												</a>
											</li>
																						<li class="report-list hidden-xs"
												data-url="https://my.bugasura.io/testReports/list/107318">
												<a href="https://my.bugasura.io/testReports/list/107318">
													<span>Sprints</span>
												</a>
											</li>
																																	<li class="issues-list hidden-xs" data-url="https://my.bugasura.io/107318/settings">
												<a href="https://my.bugasura.io/107318/settings">
													<span>Settings</span>
												</a>
											</li>
																																	<li class="show-dialog" data-appId="107318" data-project="101">
												<a>
													<span>Delete Project</span>
												</a>
											</li>
																																	<li class="show-archive-dialog" data-appId="107318" data-status="ACTIVE" data-project="101" data-team_id="79745">
												<a>
													<span> Archive  Project</span>
												</a>
											</li>
																																												<li class="show-duplicate-dialog" data-appId="107318" data-project="101" data-team_id="79745" data-team_name="DZ" data-issue_prefix="101">
												<a>
													<span>Duplicate <span class="ap__beta">Beta</span></span>
												</a>
											</li>
																					</ul>
									</div>
								</div>
								<div class="app-box" data-report-list-url="https://my.bugasura.io/issues/107318" >
									<div class="col-xs-12 logo-box">
										<div class="row answer__reports--name">
											<div class="col-xs-3 logo">
												<div class="project-icon-default-bg"></div>
																								<img loading="lazy" width="50px" height="50px" title=" Multi  Platform" data-toggle="tooltip" data-placement="top" alt="Project Icon"
																									src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/no-apps/Multiple-Multiple.svg"
													>
																							</div>
											<div class="col-xs-11 card-project-details">
												<div class="text-center">
													<h4 class="handel-over-flow app-title-107318 answer__reports-title" data-toggle="get-text">
														<span class="title handel-over-flow">101</span>
														<span class="answer__reports-private">
															<img loading="lazy" width="10px" height="14px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/blue_lock.svg" title="Private Project" data-toggle="tooltip" data-placement="top" alt="Private">
														</span>
																												<span class="answer__reports-public">
															<img loading="lazy" width="15px" height="15px" class="icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/project_type_public_black.svg" title="Public Project" data-toggle="tooltip" data-placement="top" alt="Public">
														</span>
																											</h4>
																										<span class="team-name-label handel-over-flow">
																																												DZ																																										</span>
																										<div class="answer__reports-url hidden-xs ">
														<span class="handel-over-flow" title="https://my.bugasura.io/dz/101">https://my.bugasura.io/dz/101</span>
														<div class="answer__reports-url--copy js-copy"
															data-url="https://my.bugasura.io/dz/101"
															data-toggle="tooltip" title="Copy">
															<img  src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/copy_blue.svg" alt="Copy">
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
									<div class="col-xs-12 chh-score">
																																																																																																																				<div class="col-xs-12 card__progress " data-progress-state="poor">
											<div class="card__issue-counts">
												<h5 class="card__progress-title">Open</h5>
												<span class="count open">4</span>
												<span class="count total">/4</span>
											</div>
											<div class="card__issue-separator"></div>
											<div class="card__issue-counts">
												<h5 class="card__progress-title">Closed</h5>
												<span class="count closed">0</span>
												<span class="count total">/4</span>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
									</div>
			</div>
			</div>
	</div>
		<script type="text/javascript">
		var totalAllAppsCount = 1,
		totalAndroidAppsCount = 0,
		totalIOSAppsCount = 0,
		totalAndroidMobilewebAppsCount = 0,
		totalIOSMobilewebAppsCount = 0,
		totalDesktopWebAppsCount = 0,
		totalMultipleMultipleAppsCount = 1;
		jsCurrentTeamId = `allTeams`;
		jsIsAdmin = `1`;
		jsStatus = `active`;
		jsCleanTeamName = ``;
		jsCurrentTeamName = `All Teams`;

		var prepareFilter = function(filterConfigJson) {
			var invalidTeamIdList = ``.split(',');
			var filterConfigArr = [];
			if ( filterConfigJson != '' ) {
				try {
					filterConfigArr = JSON.parse(filterConfigJson);
				} catch (error) {
					filterConfigArr = [];
					console.log(`ERROR parsing [${filterConfigJson}] to JSON`,error)
				}
			}
			var filterTemplate = ``;
			var filterSeparatorTemplate = ``;
			clearAllFilters();
			filterConfigArr.forEach(function(filter,index) {
				var filterItemTemplate = '';
				if ( typeof filter['name'] != 'undefined' && filter['name'] != '' && filter['value'] != '' ) {
					if ( filter['name'] =='teams' || filter['name'] == 'platform' ) {
						var columnName = filter['name'];
						var basicFilterLabel = filter['name'] == 'teams' ? "Teams In :&nbsp;": "Platform In :&nbsp;";
						var filterOption = 'in';
						var filterValues = filter['value'].split(',');
						filterValues.forEach(function(value) {
							if ( $(`#${columnName}_filter li a[data-value='${value}']`).length ) {
								var filterElem = $(`#${columnName}_filter li a[data-value='${value}']`),
								dataValue = filterElem.attr('data-value');
								dataTextValue = filterElem.attr('data-text-value');
								if ( filterItemTemplate != '' ){
									filterItemTemplate += `<span class="basic-filter-comma">,&nbsp;</span>`;
								}
								var invalidClass = '';
								if ( filter['name'] =='teams' && invalidTeamIdList.includes(dataValue) ){
									invalidClass = ' error';
								}
								filterItemTemplate += `<li class="searched__tag text-capitalize${invalidClass}" data-value="${dataValue}" data-filter-option="in" data-column-name="${columnName}"><span class="handel-over-flow filter-value">${dataTextValue}</span><i class="material-icons" onclick="removeSelectedFilter('${dataValue}','${columnName}')">close</i></li>`;
								filterElem.addClass('dropdown-select');
								filterElem.parent().addClass('active selected-filter-item');
							}
						});
					} else if ( filter['name'] =='type' || filter['name'] == 'status' ) {
						var columnName = filter['name'];
						var basicFilterLabel = filter['name'] == 'type' ? "Type Is :&nbsp;": "Status Is :&nbsp;";
						var filterOption = 'is';
						var filterValue = filter['value'];
						if ( $(`#${columnName}_filter li a[data-value='${filterValue}']`).length ) {
							var filterElem = $(`#${columnName}_filter li a[data-value='${filterValue}']`),
							dataValue = filterValue,
							dataTextValue = filterElem.attr('data-text-value');
							filterItemTemplate += `<li class="searched__tag text-capitalize" data-value="${dataValue}" data-filter-option="is" data-column-name="${columnName}"><span class="handel-over-flow filter-value">${dataTextValue}</span><i class="material-icons" onclick="removeSelectedFilter('${dataValue}','${columnName}')">close</i></li>`;
							filterElem.addClass('dropdown-select');
							filterElem.parent().addClass('selected-filter-item');
							// filterElem.find('label')[0].MaterialRadio.check();
							filterElem.find('input').prop('checked',true);
						}
					}
					if ( filterItemTemplate != '' ) {
						let filterSeparator = 'and';
						let filterAndSeparatorClass = `class="dropdown-select active" `;
						let filterOrSeparatorClass = '';
						if ( filter['separator'] == 'or' ){
							filterSeparator = 'or';
							filterAndSeparatorClass = '';
							filterOrSeparatorClass = `class="dropdown-select active" `;
						}
						filterSeparatorTemplate = `<div class="dropdown filter-separator">
									<button data-toggle="dropdown">
										<span class="js-text">${filterSeparator}</span>
										<span class="material-icons">&#xe313</span>
									</button>
									<ul class="dropdown-menu ap__dropdown--menu" data-toggle="update-dropdown-separator" js-used="true">
										<li>
											<a ${filterAndSeparatorClass}href="javascript:void(0);" data-separator="and">and</a>
											<span class="material-icons">&#xe876</span>
										</li>
										<li>
											<a ${filterOrSeparatorClass}href="javascript:void(0);" data-separator="or">or</a>
											<span class="material-icons">&#xe876</span>
										</li>
									</ul>
								</div>`;
						if ( filterTemplate != '' ) {
							filterTemplate += filterSeparatorTemplate;
						}
						filterTemplate += `<div class="text-capitalize basic-filter-tag-div" data-basic="${columnName}">${basicFilterLabel}${filterItemTemplate}</div>`;
					}
				}
			});
			$("#bug_report_multi_search .search_results_count").text(`1`);
			$(`#bug_report_multi_search ul.js__filter-tags .basic-filter-tag-div`).remove();
			if ( filterTemplate != '' ) {
				filterTemplate += `<div class="dropdown filter-separator hidden">
									<button data-toggle="dropdown">
										<span class="js-text">and</span>
										<span class="material-icons">&#xe313</span>
									</button>
									<ul class="dropdown-menu ap__dropdown--menu" data-toggle="update-dropdown-separator" js-used="true">
										<li>
											<a class="dropdown-select active" href="javascript:void(0);" data-separator="and">and</a>
											<span class="material-icons">&#xe876</span>
										</li>
										<li>
											<a href="javascript:void(0);" data-separator="or">or</a>
											<span class="material-icons">&#xe876</span>
										</li>
									</ul>
								</div>`;
									$(filterTemplate).insertBefore(`#bug_report_multi_search ul.js__filter-tags .filter-dets`);
								$("#bug_report_multi_search").addClass('enabled').removeClass('hidden');
				$("#project_filter_button .filter-text").addClass('hidden');
				$("#project_filter_button .filter-text").parents('button').attr('title', '');
				$("#project_filter_button .colon").addClass('hidden');
			}
			$('.filters__clear').toggleClass('hidden',!$('.js-bug-types li.selected-filter-item>a').length);
			$('#project_filter_button').removeClass('disabled');
			if ( !$('.js-bug-types li.selected-filter-item>a').length && totalAllAppsCount == 0 ){
				$('#project_filter_button').addClass('disabled');
				$('#project_filter_button').parent().removeClass('open');
			}
		}

		$(document).ready(function () {

									$(".js-create_project").removeClass('visible-hidden');
						var replaceUrl = 'https://my.bugasura.io/apps';
			if ( window.location.href != replaceUrl ) {
				window.history.pushState({url: replaceUrl}, "Bugasura: Everyone's Testing", replaceUrl);
			}
			if ( $('.js-project-filter:visible').length && $('.js-project-filter').hasClass('active') ) {
				$('.project-filters-mobile').removeClass('hidden');
			}
			$('.project-tab-js').removeClass('disable pointer-events-none');
			$("#apps_tab_container").removeClass('pointer-events-none');
			$('.project-tab-js.active').removeClass('active');
							$('.project-tab-js[data-project-tab="my_team"]').addClass('active');
				$('.project-tab-js[data-project-tab="my_team"]').addClass('pointer-events-none');
									$(".project-type-dropdown").removeClass("hidden");
								let activeTab = ` Team Projects `;
				$('.selected-tab-heading h2').text(activeTab)
						$("#apps_tab_container").removeClass('js-project-tab-loading');
							$('#my_projects .count').text(`0`);
				$('#team_projects .count').text(`1`);
				$('#contributed_projects .count').text(`1`);
				$('#all_projects .count').text(`2`);
									$("#project_team_selection .team-list-item").removeClass('dropdown-select');
			$("#project_team_selection #tm_allTeams .team-list-item").addClass('dropdown-select');
			$("#currentTeam").attr('title',`All Teams`).find('.js-text').text(`All Teams`);
			$('#currentProjectStatus .js-text').text(` Active `);
			$("#current_project_status .js-project-status").removeClass('dropdown-select');
			$("#current_project_status #active").addClass('dropdown-select');
			$("#current_project_type .project-types-js").removeClass('dropdown-select');
						   $("#current_project_type #all").addClass('dropdown-select');
			   $("#currentProjectType .js-text").text('All Type');
			
			var userId = "70292";
							var filterConfigJson = ``;
				var prepareFilterConfigJson = ``;
				var filterConfigArr = new Array();
				if ( filterConfigJson != '' ) {
					try {
						filterConfigArr = JSON.parse(filterConfigJson);
					} catch (error) {
						filterConfigArr = [];
						console.log(`ERROR parsing [${filterConfigJson}] to JSON`,error)
					}
				}
				var cookieArr = {filterConfig: filterConfigArr };
				cookieArr = JSON.stringify(cookieArr);
				// Expiry time for the cookie is set to 7days
				var d=new Date();
				d.setTime(d.getTime()+(7*24*60*60*1000));
				var expires = ";expires="+d.toGMTString();
				if ( filterConfigArr.length == 0 )
					expires = ";expires=Thu, 01 Jan 1970 00:00:00 UTC";
				document.cookie = `app_filter[${userId}]=${cookieArr}${expires};path=/;`;
				prepareFilter(prepareFilterConfigJson);
										// Set the Project Tab value to the cookies
				var cookieProjectTab = `my_team`;
				var d=new Date();
				d.setTime(d.getTime()+(7*24*60*60*1000));
				var expires = ";expires="+d.toGMTString();
				document.cookie = `project_tab[${userId}]=${cookieProjectTab}${expires};path=/;`;
			
							jsSearchText = ``.trim().replace(/ +/g, ' ');
				$('.js-input-search').val(jsSearchText);
				if ( jsSearchText !== '' ) {
					$('.new-create-block').hide();
					$('.projects-search--close').show();
				} else {
					$('.projects-search--close').hide();
					$('.new-create-block').show();
				}
						noProjectsFound();
			updatePaginationCount();
			$('.js-project_pin-unpin, [data-toggle="tooltip"]').tooltip({container:'body'});
			
							$("#first_report_modal").empty();
				$('.js-tooltip').tooltip();
						componentHandler.upgradeDom();

			// Enabling and disabling background scroll on dropdown open in mobile view
			$(".ap__dropdown--mobile-fixed").on({
				'hidden.bs.dropdown':function() {
					$('body').removeClass('hide-overflow');
				},
				'shown.bs.dropdown': function() {
					$('body').addClass('hide-overflow');
				}
			});
		});

	</script>

			</div>
			<!-- End Apps -->

			</div>
</div>


<!-- First Report Modal -->
<div class="modal fade" id="first_report_modal" role="dialog">

</div>

<div class="modal fade" id="project_delete_dailog" role="dialog" tabindex="-1">

</div>
<!-- Archive Modal -->
<div class="modal fade v-center mobile-v-center bug-report__delete-issue" id="project_archive_dailog" tabindex="-1" role="dialog" aria-labelledby="remove_team">

</div>

<!-- Invite Users Modal -->
<div class="modal fade v-center bug-report__delete-issue invite_user_modal" id="invite_user_modal" tabindex="-1" role="dialog" aria-labelledby="invite_user">

</div>
<!-- Create Team and Invite Users Modal -->
<div class="modal fade v-center bug-report__delete-issue invite_user_modal" id="create_team_invite_modal" tabindex="-1" role="dialog" aria-labelledby="create_team_invite">

</div>

<!-- Duplicate Porject modal -->
<div class="modal fade ap__modal v-center" id="project_duplicate_dailog" role="dialog" tabindex="-1">

</div>


<script type="text/javascript">
	var is_new_app = 1,
	is_new_build = 1,
	is_new_url = 0,
	is_app_farm = 1,
	is_web_farm = 0,
	maxAppsPerPage = 20,
	jsCurrentTeamId = "allTeams",
	jsIsAdmin = `1`,
	jsCleanTeamName = ``,
	jsStatus = `active`,
	jsCurrentTeamName = `All Teams`;
	teamListCount = 2;
	let projectFilter = [];
	let arrCount = 0, param = {};
	var introProjectPage = '', filterConfigJson;
	/**
	 * If the search input is empty and there are no projects, then the "no apps found" message is
	shown. If the search input is empty and there are projects, then the "no apps found" message is
	hidden. If the search input is not empty and there are no projects, then the "no apps found" message
	is hidden. If the search input is not empty and there are projects, then the "no apps found" message
	is hidden.
	*/
	function noProjectsFound() {
		var search = $.trim($(".js-input-search:visible").val()).replace(/ +/g, ' ').toLowerCase();
		$(".answer__reports").removeClass('no-apps-found');
		$('.answer__reports').each(function() {
			projectCardCount = $(this).find('.apps_block__js:not(.hidden):visible').length;
			if ( !projectCardCount && search != '' ) {
				$(this).addClass('no-apps-found');
				$(this).find('.answer__reports-no-apps').prop('hidden',false);
				$(this).find('.new-create-block').prop('hidden',true);
			} else if ( !projectCardCount && search == '' && jsStatus != 'archive' ) {
				$(this).addClass('no-apps-found');
				$(this).find('.answer__reports-no-apps').prop('hidden',true);
				$(this).find('.new-create-block').prop('hidden',false);
			} else if ( projectCardCount ) {
				$(this).removeClass('no-apps-found');
				$(this).find('.answer__reports-no-apps').prop('hidden',true);
				$(this).find('.new-create-block').prop('hidden',true);
			}
			if ($(this).is(':visible') ) {
				$(".answer__search, .header-project-search").removeClass('disable');
				if ( search == '' && !projectCardCount )
					$(".answer__search, .header-project-search").addClass('disable');
				if ( $(this).find('.new-create-block').is(':visible') ) {
					$(".ap__welcom-msg .js-create_project").addClass('hidden');
				} else {
					$(".ap__welcom-msg .js-create_project").removeClass('hidden');
				}
			}
			if ( jsStatus == 'archive' )
				archiveNoAppCheck( $(this) )
		});
	}

	/**
	 * The function updatePaginationCount() is called when the user clicks on the "All Apps" tab,
	"Android Apps" tab, "iOS Apps" tab, "Android Mobile Web" tab, "iOS Mobile Web" tab, "Desktop Web"
	tab, or the "Multiple Multiple Apps" tab.
	 *
	 * The function first checks if the user is on the "All Apps" tab. If so, it sets the variable
	totalCardsShown to the total number of all apps.
	 *
	 * If the user is on the "Android Apps" tab,
	 */
	function updatePaginationCount() {
		$(".apps_shown-count").addClass('visible-hidden');
		if ( $(".answer__reports.active").length ) {
			switch( $(".answer__reports.active").attr('id') ) {
				case "all_apps":
					totalCardsShown = totalAllAppsCount;
					break;
				case "android_apps":
					totalCardsShown = totalAndroidAppsCount;
					break;
				case "ios_apps":
					totalCardsShown = totalIOSAppsCount;
					break;
				case "android_mweb":
					totalCardsShown = totalAndroidMobilewebAppsCount;
					break;
				case "ios_mweb":
					totalCardsShown = totalIOSMobilewebAppsCount;
					break;
				case "desktop_web":
					totalCardsShown = totalDesktopWebAppsCount;
					break;
				case "multiple_multiple":
					totalCardsShown = totalMultipleMultipleAppsCount;
					break;
				default:
					return;
			}
		}
		if ( totalCardsShown > 0 && $('.project-tab-js.active:visible .count').length ) {
			var totalCardsCount = $('.project-tab-js.active:visible .count').text();
			$(".apps_shown-count #apps_total_count").text(totalCardsCount);
			$(".apps_shown-count #apps_shown_count").text(totalCardsShown);
			$(".apps_shown-count").removeClass('visible-hidden');
		}
	}

	/**
	 * The archiveNoAppCheck function is used to check if there are any apps in the archive. If there
	are none, the archiveNoApp function is called.
	 *
	 * The archiveNoApp function is used to display a message to the user that there are no apps in the
	archive.
	 *
	 * The archiveNoApp function is called in the archiveNoAppCheck function.
	 */
	function archiveNoAppCheck( thisvla ){
		switch( thisvla.attr('id') ) {
			case "all_apps":
				if ( totalAllAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "android_apps":
				if ( totalAndroidAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "ios_apps":
				if ( totalIOSAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "android_mweb":
				if ( totalAndroidMobilewebAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "ios_mweb":
				if ( totalIOSMobilewebAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "desktop_web":
				if ( totalDesktopWebAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
			case "multiple_multiple":
				if ( totalMultipleMultipleAppsCount == 0 ){
					archiveNoApp( thisvla )
				}
				break;
		}
	}

	/**
	 * The function archiveNoApp() is called when the user clicks on the "Archived" tab.
	 * It adds the class "no-apps-found" to the div with the class "answer__reports" and
	 * adds the class "hidden" to the div with the class "answer__reports-no-apps".
	 * It also adds the class "hidden" to the div with the class "new-create-block" and
	 * changes the text of the div with the class "answer__reports-no-apps" to "Looking for
	 */
	function archiveNoApp( thisvla ){
			thisvla.addClass('no-apps-found');
			thisvla.find('.answer__reports-no-apps').prop('hidden',false);
			thisvla.find('.new-create-block').addClass('hidden');
			thisvla.find('.answer__reports-no-apps .heading').text('Looking for an archived project? None so far.');
			if ( $('.answer__reports.active').attr('id') == thisvla.attr('id') ){
				$('.answer__search').addClass('disable');
			}
	}

	
	/**
	 * This function is called when the user clicks on the "Load More" button. It is used to load more
	apps from the server.
	 */
	function getProjectLists(platform, platformType, isAllApps, pageNo, totalAppsLoaded, status, projectType, searchText, isFirstLoad, isSearchFilter, isTeamSelect, projectTab ) {
		var filterConfig = getFilterConfig(),
		filterConfigJson = '';
		if (filterConfig ) {
			filterConfigJson = JSON.stringify(filterConfig);
		}
		if ( isFirstLoad )
			$("#apps_tab_container").addClass('pointer-events-none');
		$.get(`https://my.bugasura.io/apps`,{
			isAllApps: isAllApps,
			platform: platform,
			platformType: platformType,
			pageNo: pageNo,
			loadFrom: totalAppsLoaded,
			status: status,
			mode: 'ajax',
			isFirstLoad: isFirstLoad,
			isSearchFilter: 1,
			projectType: projectType,
			searchText: searchText,
			filterConfig: filterConfigJson,
			isTeamSelect: false,
			projectTab: projectTab
		},function(response) {
			// Hide the mobile dropdown
			if ( $('.js-dropdown-close').is(":visible") )
				$('.js-dropdown-close').trigger('click');

			if ( isFirstLoad ) {
				if ( isSearchFilter ) {
					$("#platform_tab_container").empty().append(response);
				} else {
					$("#platform_tab_container").empty().append(response);
				}
				var height = $(window).height() - $('.recent-apps-dashboard--bg').height() - 270;
				$('.answer__reports-no-apps').css('height',height);
				$('#current_platform>li>a.dropdown-select').click();
			} else {
				var appendDiv = '#all_apps';
				if ( appendDiv != '' ) {
					$(appendDiv).find('.apps_list_loader__js').detach();
					$(appendDiv).removeClass('loading_more__js');
					$(appendDiv).append(response);
				}
			}
			$('.project-tab-js, #apps_tab_container').removeClass('pointer-events-none');
		}, 'html');
	}

	//Calulate event spent time and send event to mixpanel
	$(window).on("beforeunload", function() {
	    if (startTime) {
		    //Prepare properties
		    eventProperty = {
		      "Page" : "Project Dashboard",
		      "Team" : "All Teams"
		    }

		  	mixPanelTimeSpent(eventProperty);
	    }
	});

	var firstReportForm;
	$(document).ready(function () {

		// Show Welcome Banner
								
		// Apply filter button only for mobile view.
		$(document).on('click', '#filter_apply', function(e) {
			var e = e,  multiSearchTemplate = ``;
			$(this).parent().addClass('disabled');
			$('#bug_report_multi_search ul.js__filter-tags div').remove();
			$('.js-bug-types li.selected-filter-item>a').each(function() {
				let filterText = $(this).find('.text').text().trim();
				let filterValue = $(this).data('value');
				let column = $(this).data('column').trim();
				let isCustomFieldFilter = typeof $(this).attr('data-is-custom-field') != "undefined" && Number($(this).attr('data-is-custom-field')) == 1 ? 1 : 0;
				if ( $(`#bug_report_multi_search ul.js__filter-tags .basic-filter-tag-div[data-basic="${column}"]`).length ) {
					multiSearchTemplate = updateFilters(e, filterText, filterValue, column, $(this), '', false, '', isCustomFieldFilter );
					$(`#bug_report_multi_search ul.js__filter-tags .basic-filter-tag-div[data-basic="${column}"]`).append(multiSearchTemplate);
				} else {
					multiSearchTemplate = updateFilters(e, filterText, filterValue, column, $(this), '', false, 'and', isCustomFieldFilter);
					// $(multiSearchTemplate).insertBefore('#bug_report_multi_search ul.js__filter-tags .save_issue_filters--js');
					$(multiSearchTemplate).appendTo('.js__filter-tags');
				}
			});

			$('#bug_report_multi_search').addClass('enabled').removeClass('hidden');
			$("#desktop_filter_button .filter-text").addClass('hidden');
			$("#desktop_filter_button .filter-text").parents('button').attr('title', '');
			$("#desktop_filter_button .colon").addClass('hidden');
			$(".selected-saved-filter").removeClass('selected-saved-filter');
			$("#bug_report_multi_search .filter-separator").removeClass('hidden');
			$("#bug_report_multi_search .filter-separator").last().addClass('hidden');

			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var searchText = '';
			if ( $('.js-input-search:visible').length )
				searchText = $('.js-input-search:visible').val().trim();
			getProjectLists('ALL', 'ALL', 1, '', '', 'ACTIVE', 'all', searchText, 1, 1, 0, projectTab );
		});

		$('.js-dropdown-close').on('click',function(e) {
			e.preventDefault();
			$('.js-project-filter').removeClass('active');
			$('#bug-report__status_dropdown').removeClass('open');
			$('#sort_filter_dropdown').removeClass('open')

			$('body').removeClass('hide-overflow');

		});

		$(document).on('click', '.js-bug-types li>a', function (e) {
			e.stopPropagation();
			var filterTextValue = $(this).data('text-value'),
			filterValue = $(this).data('value'),
			filterColumnName = $(this).data('column').trim().toLowerCase();
			let isMobile = false;

			if (filterColumnName == 'type' || filterColumnName == 'status') {
				$(this).find('input').prop('checked', true);
				if ( $(this).parent().hasClass('selected-filter-item') ) {
					return;
				} else {
					var prevValue = $('.searched__tag[data-column-name='+filterColumnName+'][data-value]').data('value');
					if ( prevValue != '' &&  prevValue != filterValue ) {
						removeSelectedFilter(prevValue,filterColumnName, false);
					}
					$('#project_filter_button').parent().addClass('open');
				}
			}
			// Add/Remove the selected filter.
			if ($(this).parent().hasClass('selected-filter-item')) {
				if (!isMobile) {
					removeSelectedFilter(filterValue, filterColumnName);
				} else {
					$(this).parent().removeClass('selected-filter-item');
				}
			} else {
				$(this).parent().addClass('selected-filter-item');
				if ( !isMobile && typeof e.which != 'undefined' && typeof e.originalEvent != 'undefined' ) {
					var multiSearchTemplate = '';
					$('#bug_report_multi_search').addClass('enabled').removeClass('hidden');
					if ( $(`#bug_report_multi_search ul.js__filter-tags .basic-filter-tag-div[data-basic="${filterColumnName}"]`).length ) {
						multiSearchTemplate = updateFilters(e, filterTextValue, filterValue, filterColumnName, $(this) , '', false, '');
						$(`#bug_report_multi_search ul.js__filter-tags .basic-filter-tag-div[data-basic="${filterColumnName}"]`).append(multiSearchTemplate);
					} else {
						multiSearchTemplate = updateFilters(e, filterTextValue, filterValue, filterColumnName, $(this) , '', false, 'and');
						$(multiSearchTemplate).insertBefore('.filter-dets');
					}
					$("#bug_report_multi_search .filter-separator").removeClass('hidden');
					$("#bug_report_multi_search .filter-separator").last().addClass('hidden');
				}
			}

			$("#project_filter_button .filter-text").addClass('hidden');
			$("#project_filter_button .filter-text").parents('button').attr('title', '');
			$("#project_filter_button .colon").addClass('hidden');
			$(".selected-saved-filter").removeClass('selected-saved-filter');
			$(".bugreport-notify-block").addClass("hidden");

			$('#filter_apply').parent().removeClass('disabled');
			$('.filters__clear').toggleClass('hidden',!$('.js-bug-types li.selected-filter-item>a').length);

			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var searchText = '';
			if ( $('.js-input-search:visible').length )
				searchText = $('.js-input-search:visible').val().trim();
			if (!isMobile) {
				getProjectLists('ALL', 'ALL', 1, '', '', 'ACTIVE', 'all', searchText, 1, 1, 0, projectTab );
			}
		});

		$(document).on("click", '.js-bug-filter-types .bug-filter-dropdown-menu .dropdown-submenu button', function(e){
			e.stopPropagation();
			e.preventDefault();
			if( $(this).next('.dropdown-menu').hasClass('current-active') )
				return;
			$(".js-bug-filter-types .dropdown-submenu .dropdown-menu").removeClass('current-active');
			$(".js-bug-filter-types .dropdown-submenu").removeClass("active-filter");
			$(this).next('.dropdown-menu').addClass('current-active');
			$(this).parents('.dropdown-submenu').addClass('active-filter');
			$(".js-bug-filter-types .dropdown-submenu .dropdown-menu:not('.current-active'):visible").removeClass('opened');
			if ( $(this).next('.dropdown-menu').hasClass('opened') ) {
				$(this).next('.dropdown-menu.opened').removeClass('opened');
			} else {
				$(this).next('.dropdown-menu').addClass('opened');
			}
			var $_this = $(this);
			setTimeout(function(){
				$_this.siblings(".dropdown-menu").find('input.js-search-list').focus();
			}, 300);
		});
		$(document).on("mouseenter", '.js-bug-filter-types .bug-filter-dropdown-menu .dropdown-submenu',function(e) {
			$(this).find('button.bug-filter-btns').trigger('click');
		});
		// Open and the filter dropdown manually.
		// So that clicling on inside it should not close
		$('#project_filter_button').on('click',function() {
			$(this).parent().addClass('open');
			if ($('.advanced-filter-cotents>.active').find('li.active input').is(':visible')) {
				$('.advanced-filter-cotents>.active').find('li.active input').not('[type="hidden"]').focus();
			}else if ( $(this).parent().find('input.js-search-list').is(':visible') ) {
				$(this).parent().find('input.js-search-list').focus();
			} else {
				$('#advanced_filter_search').focus();
			}
		});
		$('body').click(function(e) {
			var $container = $("#project_filter_button").parent();
			// if the target of the click isn't the container nor a descendant of the container
			if (!$container.is(e.target) && $container.has(e.target).length === 0) {
				$container.removeClass('open');
			}
		});
		$(document).on('click', '.filter-separator ul[data-toggle="update-dropdown-separator"] li a', function(e) {
			if ( $(this).hasClass('dropdown-select') && $(this).hasClass('active') )
				return;

			$('[data-toggle="update-dropdown-separator"]>li').removeClass('active');
			$(this).parents('ul[data-toggle="update-dropdown-separator"]').find('a').removeClass('dropdown-select active');
			$(this).addClass('dropdown-select active');
			// In mobile dropdown-backdrop will be it's previous element.
			var $button = $(this).parents('.dropdown-menu').prev('button').length ? $(this).parents('.dropdown-menu').prev('button') : $(this).parents('.dropdown-menu').prev().prev(),
				getText = $(this).clone().children().remove().end().text();
			$button.find('.js-text').detach();
			$button.contents().filter(function () {
				// Return if node type is text.
				return (this.nodeType == 3);
			}).remove();

			$button.prepend('<span class="js-text">' + getText + '</span>');
			// Get the Column name
			let columnName = $(this).parents('.dropdown').next().data('basic');

			if ( typeof e.which != 'undefined' && typeof e.originalEvent != 'undefined' ) {
				$("#project_filter_button .filter-text").addClass('hidden');
				$("#project_filter_button .filter-text").parents('button').attr('title', '');
				$("#project_filter_button .colon").addClass('hidden');
				$(".selected-saved-filter").removeClass('selected-saved-filter');
			}
			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var searchText = '';
			// if ( $('.js-input-search:visible').length )
				// searchText = $('.js-input-search:visible').val().trim();
			getProjectLists('ALL', 'ALL', 1, '', '', 'ACTIVE', 'all', searchText, 1, 1, 0, projectTab )
		});
		// Clear all filters
		$("#clear_issue_filters, .js-clear-filters").click(function(e) {
			e.preventDefault();
			clearAllFilters();
			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var searchText = '';
			if ( $('.js-input-search:visible').length )
				searchText = $('.js-input-search:visible').val().trim();
			getProjectLists('ALL', 'ALL', 1, '', '', 'ACTIVE', 'all', searchText, 1, 1, 0, projectTab );
		});
		$('.js-bug-filter-types .bug-filter-dropdown-menu .dropdown-submenu button.bug-filter-btns').first().trigger('click');
		// Click function to call a function to copy public url
		/**
		 * When the user clicks on the "Copy" button, the "copyToClipBoard" function is called. The
		function takes three arguments: the event object, the element that triggered the event, and the
		data-url attribute of the element that triggered the event.
		 */
		$(document).on('click','.app-box .js-copy', function (e) {
			var elem = $(this);
			var dataUrl = $(this).attr('data-url');
			if ( !dataUrl ) {
				elem = $(this).find('.js-copy');
				dataUrl = elem.attr('data-url');
			}
						copyToClipBoard(e, elem, dataUrl);
		});

		/**
		 * When the user clicks on the "Copy" button, the text of the link is copied to the clipboard.
		 */
		$(document).on('click','.project-link .js-copy',function(e){
			e.stopPropagation();
			e.preventDefault();

			var text = $(this).attr('data-url');
			if (!text) toastrMsg('Error while copying', 'ERROR', true);

			let $thisDropdown = $(this).parents('.dropdown');

			navigator.clipboard.writeText(text).then(function() {
				/* clipboard successfully set */
				// Show that text is copied.
				$('.bug__emails-dropdown').addClass('copied');
				// Allow to copy again
				setTimeout(function() {
					$('.bug__emails-dropdown').removeClass('copied');
					// Hide the dropdown after copied animation is done.
					$thisDropdown.find('[data-toggle="dropdown"]').trigger('click');
				},2000);
			});
		});

		
		// Function on toggle of project privacy type in project creation modal.
		$(document).on('change', '#project_type_selection', function() {
			var projName = $("#proj_name").val().trim();
			var flag = $(this).is(':checked');
			$(this).parents('.modal-body').find('.js-toggle-section').slideToggle('slow');
			if ( flag )
				return;
			cleanProjName = makeCleanPublicLink(projName);
			$("#fr_public-url").text(cleanProjName).val(cleanProjName);
		});

		// Common function of project creation and project settings when project privacy is toggled.
		$('.js-settings-project-toggle input').on('change',function() {
			var flag = $(this).is(':checked');
			$(this).parents('.modal-body').find('.js-toggle-section').slideToggle('slow');
		});

		$(document).on('click',".project__team ul.dropdown-menu a.team-list-item", function() {
			$("#proj_selected_team_error").remove();
			var selectedTeamId = $(this).attr("data-teamid"),
			selectedTeamIsAdmin = parseInt($(this).attr("data-team-is-admin"));
			$("#proj_selected_team_id").val(selectedTeamId);
			$(".project__team-btn .js-text").text($(this).text().trim()).removeClass("default-text");
			var projectType = 'private';
			if ( $('.project-types-js[data-project-type].dropdown-select').length )
				projectType = $('.project-types-js[data-project-type].dropdown-select').data('project-type');
			projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			if (selectedTeamIsAdmin) {
				$("#team_select_create .invite-user-section").removeClass('hidden');
				var selectedTeamName = $(this).text().trim(),
				cleanTeamName = makeCleanPublicLink(selectedTeamName);
				$("#clean_team_name").text(cleanTeamName);
				$("#clean_team_name").parent().attr('title','https://my.bugasura.io/'+cleanTeamName);
				if ( projectType == 'public' ) {
					document.getElementById('project_type_selection').parentElement.MaterialSwitch.off();
					$('#project_type_selection').change();
				} else {
					document.getElementById('project_type_selection').parentElement.MaterialSwitch.on();
					$(".fr__privacy, .fr__public-url").slideUp('slow');
				}
				$('.fr__private-toggle').removeClass('hidden');
			} else {
				$("#team_select_create .invite-user-section").addClass('hidden');
				$(".fr__private-toggle").addClass('hidden');
				document.getElementById('project_type_selection').parentElement.MaterialSwitch.on();
				$(".fr__privacy, .fr__public-url").slideUp('slow');
			}
		});

		$('.js-tooltip').tooltip();
		$(document).on('click','.show-dialog', function () {
			var appId = $(this).attr('data-appId');
			var projectName = $(this).attr('data-project');
			if ( !appId ) return;

			$(".loading-div").show();

			var validTeamListCount = "1";
			// Check if the modal exits and then load
			$.get('https://my.bugasura.io//modal/getProjectCommonModals',{
				appId : appId,
				projectName : projectName,
				modalName : 'project_delete',
				mode : 'html'
			}, function (response) {
				$("#project_delete_dailog").empty().append(response);
				componentHandler.upgradeAllRegistered()
			});
		});
		$(document).on('click','.show-duplicate-dialog', function () {
			var appId = $(this).attr('data-appId');
			var projectName = $(this).attr('data-project');
			var currentTeamId = $(this).attr('data-team_id');
			var issuePrefix = $(this).attr('data-issue_prefix');
			var teamName = $(this).attr('data-team_name');
			if ( !appId ) return;

			$(".loading-div").show();
			var validTeamListCount = "1";

			// Check if the modal exits and then load
			$.get('https://my.bugasura.io//modal/getProjectCommonModals',{
				appId : appId,
				projectName : projectName,
				currentTeamId : currentTeamId,
				issuePrefix : issuePrefix,
				teamName : teamName,
				modalName : 'project_duplicate',
				validTeamListCount : validTeamListCount,
				mode : 'html'
			}, function (response) {
				$("#project_duplicate_dailog").empty().append(response);
				componentHandler.upgradeAllRegistered()
			});
		});
		$(document).on('click','.show-archive-dialog', function () {
			var appId = $(this).attr('data-appId');
			var status = $(this).attr('data-status');
			var appName = $(this).attr('data-project');
			var teamId = $(this).attr('data-team_id');

			$(".loading-div").show();

			var validTeamListCount = "1";
			// Check if the modal exits and then load
			$.get('https://my.bugasura.io//modal/getProjectCommonModals',{
				appId : appId,
				status : status,
				appName : appName,
				teamId : teamId,
				modalName : 'project_archive',
				mode : 'html'
			}, function (response) {
				$("#project_archive_dailog").empty().append(response);
				componentHandler.upgradeAllRegistered()
			});
		});

		


		$(document).on('change',"#team_name", function(){
			var selectedTeamName = $("#team_name").val().trim();
			cleanTeamName = makeCleanPublicLink(selectedTeamName);
			$("#clean_team_name").text(cleanTeamName);
			$("#clean_team_name").parent().attr('title','https://my.bugasura.io/'+cleanTeamName);
		})

		$('#confirm_code_input').on("paste",function(e) {
			e.preventDefault();
		});
		
		
		// Show tools enable/disable toaster msg
		
		// Show github installation toaster msg
		

		
		
		$(document).on('click','#create_first_report_cancel', function() {
			$('#first_report_modal').modal('hide');
			document.getElementById('project_type_selection').parentElement.MaterialSwitch.on();
			$('#issues_type_selection').prop('checked', false);
			$('.js-toggle-section').hide();
		});

		$('.team-list-section').on('show.bs.dropdown', function(e){
			$('body').css('overflow','');
			if ( $(window).width() < 768 )
				$('body').css('overflow','hidden');
		});
		$('.team-list-section').on('hide.bs.dropdown', function(e){
			$('body').css('overflow','');
		});

		var height = $(window).height() - $('.recent-apps-dashboard--bg').height() - 270;
		$('.answer__reports-no-apps').css('height',height);

		$(document).on('click','#current_platform>li>a', function() {
			$(this).parents('#current_platform').find('li').removeClass('active');
			$(this).parents('li').addClass('active');
			setTimeout(function(){
				noProjectsFound();
			},200);
		});
		$('#current_platform>li>a.dropdown-select').click();

		// Project search
		$(document).on('click','.projects-search--close', function () {
			$('[data-toggle="search"]').val('');

			var platform = 'ALL',
			platformType = 'ALL',
			status = 'ACTIVE';
			var projectType = 'all';
			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var isAllApps = 1;
			getProjectLists( platform, platformType, isAllApps, '', '', status, projectType, '', 1, 1, 0, projectTab );

		});
		var searchTimeout;
		var jsSearchText = '';
		$(document).on('keyup','.js-input-search:visible',function (e) {
			var searchText = $.trim($(this).val()).replace(/ +/g, ' ');
			if ( searchText !== '' ) {
				$('.new-create-block').hide();
				$('.projects-search--close').show();
			} else {
				$('.projects-search--close').hide();
				$('.new-create-block').show();
			}
			if ( searchTimeout )
				clearTimeout( searchTimeout );
			searchTimeout = setTimeout(function() {
				if ( jsSearchText == searchText )
					return;
				jsSearchText = searchText;
				var platform = 'ALL',
				platformType = 'ALL',
				status = 'ACTIVE';
				var projectType = "";
				var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
				var isAllApps = 1;
				$('.project-tab-js').addClass('pointer-events-none');
				$("#apps_tab_container").addClass('pointer-events-none');
				getProjectLists( platform, platformType, isAllApps, '', '', status, projectType, searchText, 1, 1, 0, projectTab );
			}, 1000 );
		});

		$('.projects-header-search--close').on('click',function () {
			$("#filter-value, #table_filter_value").val("");
			$('.js-input-search').val('');
			$('.navbar .search-bar').addClass('hidden');

			var platform = 'ALL',
			platformType = 'ALL',
			status = 'ACTIVE';
			var projectType = '';
			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var isAllApps = 1;
			getProjectLists( platform, platformType, isAllApps, '', '', status, projectType, '', 1, 1, 0, projectTab );

		});

		$(window).scroll(function() {
			if( $(window).scrollTop() >= $(document).height() - ( $(window).height() + 100 ) ) {
				// If the active tab is having loading_more class then return from the function.
				if ( $('#all_apps').hasClass('loading_more__js') ||
					 $('#all_apps').hasClass('loading_error_js') )
					return;
				$('#all_apps').addClass('loading_more__js');
				var platform = 'ALL',
				platformType = 'ALL';
				totalAppsLoaded = $('#all_apps .apps_block__js').length;
				appendDiv = '#all_apps';
				isAllApps = 1;
				if ( totalAppsLoaded >= totalAllAppsCount ) {
					$(appendDiv).removeClass('loading_more__js');
					return;
				}
				// Show the loading div at the bottom of the appendDiv and add 'loading_more' class to the active tab.
				loaderDiv = `<div class="ap__loader apps_list_loader__js" data-html2canvas-ignore="true">
								<img alt="loading" src=https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/Loader.gif >
							</div>`;
				$(appendDiv).append(loaderDiv);
				currPageNo = Math.floor(totalAppsLoaded/maxAppsPerPage);
				var projectType = 'all',
				projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab'),
				status = 'ACTIVE',
				searchText = '';
				if ( $('.js-input-search:visible').length )
					searchText = $('.js-input-search:visible').val().trim();
				$('.project-tab-js').addClass('pointer-events-none');
				$(".answer__tools").addClass('pointer-events-none');
				getProjectLists( platform, platformType, isAllApps, currPageNo, totalAppsLoaded, status, projectType, searchText, 0, 0, 0,projectTab );
			}
		});
		

		$(document).on('click','.answer__reports .js-my-project-add-remove', function () {
			var projectId = $(this).data('app_id');
			var teamId = $(this).data('team_id');
			var projectName = $(this).data('app_name');
			
			var showToasterMsg = 1;

			if ( $(`.js-app-favourite_add_remove[data-app_id="${projectId}"`).hasClass("dont-show-toaster") )
				showToasterMsg = 0;

			if ( !projectId || $(this).hasClass('disabled') )
				return;

			$(this).addClass('disabled');

			IsAddProject = 1;
			if ( $(this).hasClass("ap__project-favourite_added") )
				IsAddProject = 0;

			var $_this= $(this);
			$.post('https://my.bugasura.io//account/updateUserMyProjectSettings',{
				projectId	 : projectId,
				teamId		 : teamId,
				IsAddProject : IsAddProject,
				projectName  : projectName
			},function(response){
				$_this.removeClass('disabled');
				if ( response.status == 'OK' ) {
					totalMyProjectCount = Number($('#my_projects:visible .count').text());
					$(`.answer__reports.active .apps_block__js[data-app_id='${projectId}']`).each(function(){
						if ( response.IsAddProject == 1 ) {
							$(this).addClass("ap__project-favourite_added");
							$(this).find('.js-app-favourite_add_remove').addClass('ap__project-favourite_added ').removeClass('ap__project-favourite_remove').attr('data-original-title','Remove this project from my favourites').tooltip();
							$(this).find('.js-app-favourite_add_remove img:not(.favourite_project__remove)').attr('src',`https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/my_favourite_project.svg`);
							totalMyProjectCount = Number($('#my_projects:visible .count').text());
							totalMyProjectCount++;

							projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
							if ( projectTab != "my_project" ) {

																	animationClass = getProjectCardAnimationClass(projectId);
									var width = $(`.answer__reports.active .apps_block__js[data-app_id="${projectId}"] .new-grid-card`).width();
									$(`.answer__reports.active .apps_block__js[data-app_id="${projectId}"] .new-grid-card`).addClass("project-clone-parent-div").width(width).clone(true).appendTo(`.apps_block__js[data-app_id="${projectId}"]`).addClass(`animated-div-${projectId} hidden`);
									$(`.animated-div-${projectId}`).addClass(`animate__animated ${animationClass}`).removeClass("hidden");
									setTimeout(function() {
										$(`.answer__reports.active .apps_block__js[data-app_id="${projectId}"] .new-grid-card`).removeClass("project-clone-parent-div");
										$(`.answer__reports.active .apps_block__js[data-app_id="${projectId}"] .animated-div-${projectId}`).remove();
									},1500);
								
							}

						} else {
							$(this).removeClass("ap__project-favourite_added");
							$(this).find('.js-app-favourite_add_remove').removeClass('ap__project-favourite_added ').addClass('ap__project-favourite_remove').attr('data-original-title','Add this project to my favourites').tooltip();
							$(this).find('.js-app-favourite_add_remove img:not(.favourite_project__remove)').attr('src',`https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/favourite_project.svg`);

							projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');

							totalMyProjectCount = Number($('#my_projects:visible .count').text());
							totalMyProjectCount--;
							if ( projectTab == "my_project" ) {
								$(`answer__reports.active .apps_block__js[data-app_id="${projectId}"]`).fadeOut(400);
								$(`.apps_block__js[data-app_id="${projectId}"]`).remove();

								if ( !totalMyProjectCount )
									noProjectsFound();
							}

						}
					});

					$('#my_projects .count').text(`${totalMyProjectCount}`);
					if ( response.IsAddProject == 1 ) {
						$('#my_projects').removeClass('animate__animate animate__heartBeat');
						setTimeout(function() {
							$('#my_projects').addClass('animate__animate animate__heartBeat');
						},1000);
					}

					if ( showToasterMsg )
						toastrMsg(response.message, 'success', true);
				} else{
					if ( showToasterMsg )
						toastrMsg(response.message, 'error', true);
				}
			},'json');
		});

		$(document).on('click','.answer__reports .js-project_pin-unpin', function () {
			var appId = $(this).data('app_id');
			var teamId = $(this).data('team_id');
			
			if ( !appId || $(this).hasClass('disabled') )
				return;
			$(this).addClass('disabled');
			var isPinned = 0;
			if ( $(this).hasClass('ap__project-unpin') )
				isPinned = 1;
			var $_this= $(this);
			$.post('https://my.bugasura.io/apps/updateProject',{
				appId	: appId,
				teamId	: teamId,
				isPinned: isPinned
			},function(response){
				$_this.removeClass('disabled');
				if ( response.status == 'OK' ) {
					$(`.apps_block__js[data-app_id='${appId}']`).each(function(){
						if ( response.isStarred == 1 ) {
							$(this).fadeOut(300).prependTo($(this).parents('.answer__reports')).fadeIn(300);
							$(this).addClass('js-app-pinned');
							$(this).find('.js-project_pin-unpin').addClass('ap__project-pinned').removeClass('ap__project-unpin').attr('data-original-title','Unpin').tooltip();

							$(this).find('.js-project_pin-unpin img:not(.project__unpin)').attr('src',`https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/pinned_vertical.svg`);
						} else {
							$(this).fadeOut(300).insertAfter($(this).parents('.answer__reports').find(' .apps_block__js.js-app-pinned').last()).fadeIn(300);
							$(this).removeClass('js-app-pinned');
							$(this).find('.js-project_pin-unpin').removeClass('ap__project-pinned').addClass('ap__project-unpin').attr('data-original-title','Pin').tooltip();

							$(this).find('.js-project_pin-unpin img:not(.project__unpin)').attr('src',`https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/pin_vertical.svg`);
						}
					});
					var pos = $(`.answer__reports.active .apps_block__js[data-app_id='${appId}']`).offset().top-50;
					$('body, html').animate({scrollTop:  pos});
					toastrMsg(response.message, 'success', true);
				} else{
					toastrMsg(response.message, 'error', true);
				}
			},'json');
		});


		var teamName  = $('.header-team__name').text();
		var metadata = {
			team_name: teamName
		};

		$('.report-list').on('click', function () {
			var url = $(this).attr('data-url');
			window.location.replace(url);
		});

		$('.testplan-list').on('click', function () {
			var url = $(this).attr('data-url');
			window.location.replace(url);
		});


		$(document).on('click','.create-functional-report.js-create_project.first-report-creation , .create-functional-report', function () {
						$(".loading-div").show();
			platform = $(this).data('platform');
			platformType = $(this).data('platformtype');

			var validTeamListCount = "1";
			// Check if the modal exits and then load
			$.get('https://my.bugasura.io//modal/getCreateProjectModal',{
				platform : platform,
				platformType : platform,
				currentTeamName : jsCurrentTeamName,
				validTeamListCount : validTeamListCount,
				currentTeamId : jsCurrentTeamId,
				isAdmin : jsIsAdmin,
				mode : 'html'
			}, function (response) {
				$("#first_report_modal").empty().append(response);
				$("#clean_team_name").text(jsCleanTeamName);
				$("#clean_team_name").parent().attr("title",`https://my.bugasura.io/${jsCleanTeamName}`);
				componentHandler.upgradeAllRegistered()
			});
			$('#first_report_modal').modal('show');
			$(".loading-div").hide();
		});

		// Function triggered when project creation modal is shown.
		$('#first_report_modal').on('show.bs.modal',function() {
			$("#clean_proj_name_error").css('display', '').addClass('hidden');
			$("#clean_team_name").text(jsCleanTeamName);
			$("#clean_team_name").parent().attr("title",`https://my.bugasura.io/${jsCleanTeamName}`);
		});

		$(document).on('click', '.js-platform-selection .panel-body', function(){
			$('.js-platform-selection .panel-body').removeClass("active");
			$(this).addClass("active");
		});


		$(document).on('keyup','input#proj_name', function(e) {
			if ( e.keyCode == 13 ) {
				e.preventDefault();
				$('#create_first_report').click();
			}
		});


		// Function to add href and text for the specifc platform and platformType.
		$('.first-tab a').on('click', function () {
			var platformType = $(this).attr('data-platformtype');
			var platform = $(this).attr('data-platform');
			if ($(this).attr('href') == '#no_apps') {

							$('#no_apps').find('a').attr('href', 'https://my.bugasura.io/testplans/create/' + platformType + '/' + platform);
				var noAppsBtn = 'Create Testplan for ' + platform;
				if ($(this).attr('data-platformtype') != 'Apps') {
					$('.answer__reports-no-apps .js-no-apps').html('<span class="heading">No Web-Apps Found</span> <br> Proceed to test your Web-App');

				} else {
					$('.answer__reports-no-apps .js-no-apps').html('<span class="heading">No Apps Found</span> <br> Proceed to Upload a Build');
				}

			

			if ( platformType == 'Apps' ){
					noAppsBtn += ' App';
				} else if ( platformType == 'Mobileweb' ) {
					noAppsBtn += ' Mobile Web';
				} else {
					noAppsBtn += ' Web';
				}
				$('#no_apps').find('a').text(noAppsBtn);
			}

							if ( platformType == 'Apps' && platform == 'Android' ) {
					$(".apps__add-testing a.js-create-robotium, .apps__add-testing").removeClass('hidden');
					$(".apps__add-testing a.js-checklist-testing").removeClass('on-2nd-top');
					$(".apps__add-testing a.js-checklist-testing").addClass('apps__float-btn--3');
					$(".apps__add-testing a.js-checklist-testing").removeClass('apps__float-btn--4');
				} else if ( platformType == 'Apps' && platform == 'iOS' ) {
					// $(".apps__add-testing a.js-create-robotium").removeClass('hidden');
					// $(".apps__add-testing a.js-create-human").addClass('hidden');
					// $(".apps__add-testing a.js-create-human").removeClass('apps__float-btn--4');
					// $(".apps__add-testing a.js-checklist-testing").addClass('apps__float-btn--3');
					// $(".apps__add-testing a.js-create-robotium").attr('href', 'https://my.bugasura.io/testplans/create/Apps/iOS?reportType=Bot');
					$(".apps__add-testing a.js-create-appium").attr('href', 'https://my.bugasura.io/testplans/create/Apps/iOS?reportType=Automation');
					$(".apps__add-testing a.js-checklist-testing").addClass('on-2nd-top');
					$(".apps__add-testing a.js-checklist-testing").removeClass('apps__float-btn--3');
					$(".apps__add-testing a.js-checklist-testing").addClass('apps__float-btn--4');
					$(".apps__add-testing a.js-create-robotium, .apps__add-testing a.js-create-human").addClass('hidden');
					// $("#functional-report").attr("data-platform",platform)
					// $("#functional-report").attr("data-platformType",platformType)
					//$(".apps__add-testing a.js-create-appium").attr('href', 'https://my.bugasura.io/testplans/create/' + platformType + '/' + platform);
				} else{
					$(".apps__add-testing a.js-checklist-testing").addClass('on-2nd-top');
					$(".apps__add-testing a.js-checklist-testing").removeClass('apps__float-btn--3');
					$(".apps__add-testing a.js-checklist-testing").addClass('apps__float-btn--4');
					//$(".apps__add-testing a.js-create-robotium, .apps__add-testing a.js-create-human").addClass('hidden');
					$(".apps__add-testing a.js-create-appium").attr('href', 'https://my.bugasura.io/testplans/create/' + platformType + '/' + platform);
				}
			
		});
		$('.first-tab a.active').click();


		$(document).on('click','.app-box',function (e) {
			listUrl = $(this).attr('data-report-list-url');
						if ( listUrl && $(this).parents('.new-grid-card').hasClass('public-card') ) {
				listUrl = $(this).parents('.new-grid-card.public-card').find('.answer__reports-url--copy').attr('data-url');
									if ( $(e.target).parents('.new-grid-card').hasClass('no-reports') ) {
						listUrl += "/sprints";
					}
							}
			if ( listUrl )
				window.location.href = listUrl;
		});
		$(document).on('click','.select-box',function (e) {
			var listUrl = '';
			if ( $(e.target).hasClass('select-box') ) {
				listUrl = $(e.target).attr('data-report-list-url');
			} else if ( $(e.target).hasClass('team-name-label') ) {
				listUrl = $(e.target).parent('.select-box').attr('data-report-list-url');
			}

			
			if ( listUrl && $(e.target).parents('.new-grid-card').hasClass('public-card') ) {
				listUrl =  $(e.target).parents('.new-grid-card.public-card').find('.answer__reports-url--copy').attr('data-url');

									if ( $(e.target).parents('.new-grid-card').hasClass('no-reports') ) {
						listUrl += "/sprints";
					}
							}
			if ( listUrl )
				window.location.href = listUrl;
		});

		var platformTabCount = 6;


		$('#first_report_modal').on('hidden.bs.modal', function () {
			firstReportForm.resetForm();
			document.getElementById('project_type_selection').parentElement.MaterialSwitch.on();
			$('#issues_type_selection').prop('checked', false);
			$('.js-toggle-section').hide();
			$("#team_select_create .invite-user-section").addClass('hidden');
		});

		$('#signup_welcome_modal').on('hidden.bs.modal', function () {
			var replaceUrl = window.location.href.replace('?isSignUp=1','');
			replaceUrl = replaceUrl.replace('isSignUp=1','');
			window.history.pushState({url: replaceUrl}, 'My Projects', replaceUrl);
		});

		
		// Choose the Project Tab.
		$(document).on('click','.project-tab-js[data-project-tab]', function(e) {
			if ( $(this).hasClass('pointer-events-none') || $(this).hasClass('disable') || $(this).hasClass('active') )
				return;
			// e.preventDefault();
			var $this = $(e.currentTarget);
			var projectType = $(this).data('project-type'),
			status = $('#current_project_status .dropdown-select').attr('id');
			projectTab = $(this).data('project-tab'),
			searchText = '';
			if ( $('.js-input-search:visible').length )
				searchText = $('.js-input-search:visible').val().trim();
			var platform = '',
			platformType = ''
			isAllApps = 1;
			if ( $('.app-category-tab--js.dropdown-select[data-platform]').length ) {
				isAllApps = 0;
				platform = $('.app-category-tab--js.dropdown-select[data-platform]').attr('data-platform').trim();
				platformType = $('.app-category-tab--js.dropdown-select[data-platform]').attr('data-platformtype').trim();
				if ( platform+"-"+platformType == 'ALL-ALL' )
					isAllApps = 1;
			}

						// Update the UI
			$('.project-tab-js').addClass('disable');
			$("#apps_tab_container").addClass('pointer-events-none');

			// Show the clicked tab element into the view.
			if( projectType == 'all' || projectType == 'private' ){
				$('.js-window-top-element').animate({scrollLeft: 0}, 500);
			}else{
				$('.js-window-top-element').animate({scrollLeft: $this.position().left}, 500);
			}
			getProjectLists( platform, platformType, isAllApps, '', '', status, projectType, searchText, 1, 0, 0, projectTab );
		});

		
	});

	function clearAllFilters() {
		$(`.searched__tag`).remove();
		$('.filter-separator').remove();
		$('.basic-filter-tag-div').remove();
		$('#bug_report_multi_search').addClass('hidden').removeClass('enabled');
		$(".js-bug-types li").removeClass('active selected-filter-item');
		$(".js-bug-types li a").removeClass('dropdown-select');
		$(".project-types-js>input, .js-project-status>input").each(function() {
			$(this).prop('checked', false)
			// $(this)[0].MaterialRadio.uncheck();
		});

		$("#project_filter_button .filter-text").text('').addClass('hidden');
		$("#project_filter_button .filter-text").parents('button').attr('title', '');
		$("#project_filter_button .colon").addClass('hidden');
		$(".selected-saved-filter").removeClass('selected-saved-filter');
	}

	function getFilterConfig() {
		var filterConfig = [];
		var arrCount = 0;
		if ( $("#bug_report_multi_search").hasClass('enabled') ) {
			$("li.searched__tag").each(function() {
				_this = $(this);
				currColName = $(this).attr('data-column-name');
				currValue = $(this).attr('data-value');
				if ( typeof filterConfig[arrCount] == 'undefined' ){
					filterConfig[arrCount] = {};
				}
				if ( typeof filterConfig[arrCount].name == 'undefined' ) {
					var separator = 'and';
					if ( _this.parent().prev().hasClass('filter-separator') ) {
						separator = _this.parent().prev().find('.js-text').text().toLowerCase();
					}
					if ( separator != 'and' && separator != 'or' )
						separator = 'and';
					filterConfig[arrCount].option = 'in';
					if ( currColName == 'status' || currColName == 'type' )
						filterConfig[arrCount].option = 'is';
					filterConfig[arrCount].value = currValue;
					filterConfig[arrCount].separator = separator;
					filterConfig[arrCount].name = currColName;
					if ( arrCount == 0 )
						filterConfig[arrCount].separator = 'and';
				} else {
					filterConfig[arrCount].value += ","+currValue;
				}

				if ( !_this.next().length ){
					arrCount++;
				}
			});
		}
		return filterConfig;
	}

	function updateFilters(e, filterText, filterValue, column, $this, filterCondition, isAdvanceFilter, filterSeparator ) {
		var customFieldFilterClass = '', dataDisplayName = '';
		var basicFilterTemplate = '';
		if ( ( typeof $this.attr('data-is-custom-field') != "undefined" && Number($this.attr('data-is-custom-field')) == 1 ) ) {
			if ( $this.hasClass('js-jira-filter') ) {
				dataDisplayName = ` data-display-name="jira_issue"`;
				customFieldFilterClass = 'custom_field_filter ';
			} else {
				dataDisplayName = ` data-display-name="zoho_task"`;
				customFieldFilterClass = 'custom_field_filter ';
			}
		}

		basicFilterTemplate = `<li class="searched__tag ${customFieldFilterClass}"
			data-value="${filterValue}" data-filter-option="is"
			data-column-name="${column}"${dataDisplayName}><span class="handel-over-flow filter-value">${filterText}</span>
			<i class="material-icons" onClick="removeSelectedFilter('${filterValue}','${column}')">close</i>
		</li>`;

		if ( filterSeparator != '' ) {
			var filterAndSeparatorClass = '',
			filterOrSeparatorClass = '',
			basicFilterLabel = '';
			filterSeparator = filterSeparator.toLowerCase().trim();
			if ( filterSeparator != 'and' && filterSeparator != 'or' )
				filterSeparator = 'and';
			if ( filterSeparator == 'and' ) {
				filterAndSeparatorClass = `class="dropdown-select active" `;
			} else {
				filterOrSeparatorClass = `class="dropdown-select active" `;
			}
			switch( column ) {
				case "teams":
					basicFilterLabel = "Teams In :&nbsp;";
					break;
				case "type":
					basicFilterLabel = "Type Is :&nbsp;";
					break;
				case "platform":
						basicFilterLabel = "Platform :&nbsp;";
					break;
				case "status":
					basicFilterLabel = "Status Is :&nbsp;";
					break;
			}
			var multiSearchTemplate = `<div class="text-capitalize basic-filter-tag-div" data-basic="${column}">${basicFilterLabel}${basicFilterTemplate}</div>
										<div class="dropdown filter-separator">
											<button data-toggle="dropdown">
												<span class="js-text">${filterSeparator}</span>
												<span class="material-icons">&#xe313</span>
											</button>
											<ul class="dropdown-menu ap__dropdown--menu" data-toggle="update-dropdown-separator" js-used="true">
												<li>
													<a ${filterAndSeparatorClass}href="javascript:void(0);" data-separator="and">and</a>
													<span class="material-icons">&#xe876</span>
												</li>
												<li>
													<a ${filterOrSeparatorClass}href="javascript:void(0);" data-separator="or">or</a>
													<span class="material-icons">&#xe876</span>
												</li>
											</ul>
										</div>`;
		} else {
			var multiSearchTemplate = "<span class='basic-filter-comma'>,&nbsp;</span>"+basicFilterTemplate;
		}
		return multiSearchTemplate;
	}
	//Trigger removeFilter function
	function removeSelectedFilter(dataValue, dataColumnName, isGetProject = true) {
		if ( $(`.searched__tag[data-value="`+dataValue+`"][data-column-name="`+dataColumnName+`"]`).prev().hasClass('basic-filter-comma') )
			$(`.searched__tag[data-value="`+dataValue+`"][data-column-name="`+dataColumnName+`"]`).prev().remove();
		if ( dataValue == "unassigned" &&  $(`#bug_report_multi_search .searched__tag[data-value="${dataValue}"][data-column-name="${dataColumnName}"]`).next().hasClass('filter-separator') )
				$(`#bug_report_multi_search .searched__tag[data-value="${dataValue}"][data-column-name="${dataColumnName}"]`).next().remove();
		if ( dataColumnName == "customfieldassigned" &&  $(`#bug_report_multi_search .searched__tag[data-value="${dataValue}"][data-column-name="${dataColumnName}"]`).next().hasClass('filter-separator') )
			$(`#bug_report_multi_search .searched__tag[data-value="${dataValue}"][data-column-name="${dataColumnName}"]`).next().remove();
		$(`.searched__tag[data-value="`+dataValue+`"][data-column-name="`+dataColumnName+`"]`).remove();
		$(`.selected-filter-item a[data-column="${dataColumnName}"][data-value="${dataValue}"]`).removeClass('dropdown-select');
		if ( dataColumnName == 'status' || dataColumnName == 'type' ){
			// $(`.selected-filter-item a[data-column="${dataColumnName}"][data-value="${dataValue}"] label`)[0].MaterialRadio.uncheck();
			$(`.selected-filter-item a[data-column="${dataColumnName}"][data-value="${dataValue}"] input[type='radio']`).prop('checked',false);

		}
		$(`.selected-filter-item a[data-column="${dataColumnName}"][data-value="${dataValue}"]`).parent().removeClass('active selected-filter-item');
		if ( $(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"] li`).length == $(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"] .basic-filter-comma`).length &&
			$(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"] li`).length > 0 ){
			$(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"] .basic-filter-comma`)[0].remove();
		}
		if ( !$(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"] li`).length ) {
			if ( $(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"]`).next().hasClass('filter-separator') )
				$(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"]`).next().remove();
			$(`#bug_report_multi_search .basic-filter-tag-div[data-basic="${dataColumnName}"]`).remove();
		}
		if ( !$(".js__filter-tags .searched__tag").length ) {
			$('#bug_report_multi_search').addClass('hidden').removeClass('enabled');
		}
		$("#bug_report_multi_search .filter-separator").removeClass('hidden');
		$("#bug_report_multi_search .filter-separator").last().addClass('hidden');

		$("#project_filter_button .filter-text").addClass('hidden');
		$("#project_filter_button .filter-text").parents('button').attr('title', '');
		$("#project_filter_button .colon").addClass('hidden');
		$(".selected-saved-filter").removeClass('selected-saved-filter');
		if ( isGetProject ) {
			var projectTab = $('.project-tab-js[data-project-tab].active').data('project-tab');
			var searchText = '';
			if ( $('.js-input-search:visible').length )
				searchText = $('.js-input-search:visible').val().trim();
			getProjectLists('ALL', 'ALL', 1, '', '', 'ACTIVE', 'all', searchText, 1, 1, 0, projectTab );
		}
	}

	function getProjectCardAnimationClass( projectId ) {
		var cardWidth;
		cardWidth = $(`.answer__reports.active .apps_block__js[data-app_id="${projectId}"] .new-grid-card`).width();
		containerWidth = $('#platform_tab_container').width();
		cardRatio = Math.floor(Number((containerWidth)/(cardWidth)));
		cardPosition = $(".answer__reports.active > .apps_block__js").index($(`.answer__reports.active > .apps_block__js[data-app_id="${projectId}`));
		cardPosition = cardPosition + 1;

		rowPosition = Math.ceil(Number((cardPosition)/(cardRatio)));
		columnPosition =Number((cardPosition)%(cardRatio));

		if ( columnPosition == 0 )
			columnPosition = cardRatio;
		else if ( columnPosition > 4 )
			columnPosition = 4;

		if ( rowPosition <= 0 )
			rowPosition = 1
		else if ( rowPosition > 3 )
			rowPosition = 3;

		return `card_animation_row_${rowPosition}_column_${columnPosition}`;
	}

	// Function which triggers to copy the public url to clipboard and show the neccessary tooltip.
	function copyToClipBoard(e,_this, url) {
		e.stopImmediatePropagation();
		copyToClipboard(url);
		_this.attr('title', 'Copied')
		.tooltip('fixTitle')
		.tooltip('show');
		setTimeout( function(){
			_this.attr('title', 'Copy')
			.tooltip('fixTitle')
			.tooltip('hide');
		},2000);
	}

	function handleProjectCount( appId, isPublic, isDelete, isUserFavouriteProject ) {
		var totalProjectsCount = Number($('#all_projects:visible .count').text()),
		totalMyTeamCount = Number($('#team_projects:visible .count').text()),
		totalMyFavouritProjectCount = Number($('#my_projects:visible .count').text());
		if ( isDelete ) {
			totalProjectsCount--;
			totalMyTeamCount--;

			if ( totalProjectsCount < 0 )
				totalProjectsCount = 0;

			if ( totalMyTeamCount < 0 )
				totalMyTeamCount = 0;

			if ( isUserFavouriteProject )
				totalMyFavouritProjectCount--;

			if ( totalMyFavouritProjectCount < 0 )
				totalMyFavouritProjectCount = 0;


		} else {
			if ( isPublic ) {
				if ( $('.project-types-js[data-project-type].dropdown-select').data('project-type') == 'private' ) {
					$(`.apps_block__js[data-app_id="${appId}"]`).fadeOut(250,function(){$(this).remove();});
				}
			} else {
				if ( $('.project-types-js[data-project-type].dropdown-select').data('project-type') == 'public' ) {
					$(`.apps_block__js[data-app_id="${appId}"]`).fadeOut(250,function(){$(this).remove();});
				}
			}
		}
		$('#all_projects .count').text(totalProjectsCount);
		$('#team_projects .count').text(totalMyTeamCount);
		$('#my_projects .count').text(totalMyFavouritProjectCount);
		updatePaginationCount();
	}


	
</script>
</div>
			</div>
			<!-- Load the comman files or shared files after the content is loaded -->
							




<div class="modal fade app__teams-modal" id="maintainance_banner" tabindex="-1" role="dialog" aria-labelledby="creat_team">
	<div class="modal-dialog modal-md" role="document">
		<div class="modal-content">
			<div class="modal-body">
				<img loading="lazy" width="1263px" height="946px" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/down-time.jpeg" class="img-responsive" alt="Down Time Image">
				<h4 class="modal-title text-center">We're busy pushing out some new concotions and formulas. We'll be back soon... assuming all reactions are stable.<span class="js-remove-uer"></span> </h4>
			</div>
		</div>
	</div>
</div>

<!-- The below sprint-create-form model is not required for any other page except report list -->


<!-- Image zoom modal -->
<div class="modal zoomed-view" id="img_zoom_effect" role="dialog">
	<div class="modal-card-img">
		<img loading="lazy" width="491px" height="300px" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/trail_expired.svg" onerror="this.onerror=null;this.src='https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/trail_expired.svg';" >
	</div>
</div>

	<!-- New Features Popup modal -->
	<div class="modal left fade in" id="new_features_popup" role="dialog">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-header">
					<p>New Features</p>
					<button class="mdl-button mdl-js-ripple-effect mdl-js-button close" data-dismiss="modal">
						<i class="material-icons" aria-hidden="true" >close</i>
					</button>
				</div>
				<div class="modal-body scroll u-dis-f-rc">
					<div class="u-dis-f-rc">
						<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/Loader.gif" class="img-responsive release-notes-loader">
					</div>

				</div>

			</div>
		</div>
	</div>
	

	<!-- Intimate free change plan after trial ends banner -->
	<div class="modal fade v-center" id="notify_end_trial_free_bugasura_modal" role="dialog" tabindex="-1" data-keyboard="false" data-backdrop="static">
		<div class="modal-dialog modal-sm vertical-alignment-helper">
			<div class="vertical-align-center">
				<div class="modal-content">
					<div class="modal-header padding-zero">
						<!-- <button type="button" data-dismiss="modal" class="close">
							<i class="material-icons">close</i>
						</button> -->
						<img class="sb__illustration" loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/support_bugasura_illustration.svg" alt="Illustration">
					</div>
					<div class="modal-body padding-zero">
						<p class="sb__title">Upgrade Plan</p>
						<p class="sb__desc">Your team owner needs to upgrade the account for you to continue to use <strong>Bugasura</strong>.</p>
						<a class="ap__btn ap__btn--new ap__btn--primary mdl-button mdl-js-button mdl-js-ripple-effect" id="notify_team_owner_trial_ended" type="button">Ask Owner</a>
					</div>
				</div>
			</div>
		</div>
	</div>

	<!-- For New Features Released Popup modal -->
	<div class="modal fade ap__modal v-center nf__modal" id="new_features_released_modal"  data-backdrop="static" role="dialog" tabindex="-1">
	</div>

	<!-- Product Hunt Modal -->
	<div class="modal fade ap__modal v-center nf__modal" id="product_hunt_modal"  data-backdrop="static" role="dialog" tabindex="-1">
		<div class="modal-dialog">
			<div class="modal-content padding-zero">
				<div class="modal-body">
					<button class="close ap__modal-close" data-dismiss="modal">
						<i class="material-icons">close</i>
					</button>
					<div class="row js-nf-block">
						<div class="col-xs-12">
							<div class="nf__white" data-img="">
																								<img class="img-responsive nf__image new-feature-img aniamted scale-in-center" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/new-feature/bugasuraSpacesLaunch.svg" onerror="this.onerror=null;this.src='https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/new-feature/default-feature.svg';">
								<div class="nf-ribbon-end hidden"></div>
								<div class="nf-red-ribbon">
									<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/red_ribbon.svg">
								</div>
							</div>
						</div>
						<div class="col-xs-12 animated scale-in-center">
							<div class="nf__blue text-center">
								<p class="nf__blue-title">
									<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/rocket_icon.svg">
									Launching Bugasura Spaces
									<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/party_icon.svg">
								</p>
								<p class="nf__blue-sub-title scroll-thin scroll--transparent">Join our exclusive community for like-minded developers, testers, CTOs and tech leaders.</p>
								<div class="modal-card-ext-bar">
									<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__btn ap__btn--new ap__btn--primary nf-explore-btn" id="support_launch_btn" href="https://join.slack.com/t/bugasuraspaces/shared_invite/zt-1x4b7k65i-tsxVGwoVj3DzjHAqNe_OpQ" target="_blank">
										<p class="blog-link-text">Get Your Invite</p>
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

<!-- ContextualAIUpload Modal -->
<div id="project_contextual_ai_modal"></div>

<!-- Show the comment images -->
<div class="modal fade v-center zoomed-image" tabindex="-1" role="dialog" id="issue_comment_image_preview_modal">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header preview-image-header">
				<div id="issue_comment_image_preview_user" class="icon"></div>
				<p id="issue_comment_image_preview_time"></p>
				<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__modal-close" data-dismiss="modal">
					<i class="material-icons">close</i>
				</button>
			</div>
			<div class="modal-body scroll">
				<div class="u-dis-f-rc box" id="box">
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect js-img-button prev arrow">
						<i class="material-icons">&#xe5cb</i>
					</button>
					<div class="preview-image-holder">
						<img src="" alt="Image" id="issue_comment_image_preview" class="img-responsive">
					</div>
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect js-img-button next arrow">
						<i class="material-icons">&#xe5cc</i>
					</button>
				</div>
				<p class="preview-image-counter text-center">
					<span class="current ap__text"></span> /  <span class="total ap__text"></span>
				</p>
			</div>
		</div>
	</div>
</div>
<!-- Show the Issue screenshot tab's images -->
<div class="modal fade v-center zoomed-image" tabindex="-1" role="dialog" id="issue_screenshot_preview_modal">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header preview-image-header">
				<div class="icon js-user-image"></div>
				<p class="js-user-image-time zoomed-image-time"></p>
				<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__modal-close" data-dismiss="modal">
					<i class="material-icons">close</i>
				</button>
			</div>
			<div class="modal-body scroll">
				<div class="u-dis-f-rc box">
					<a href="#issue_screenshot_preview" class="mdl-button mdl-js-button mdl-js-ripple-effect prev arrow" role="button">
						<i class="material-icons">&#xe5cb</i>
					</a>
					<div id="issue_screenshot_preview" class="carousel slide sa__carousel carousel-fade" data-ride="carousel">
						<div class="carousel-inner">
							<div class="item active">
								<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/Loader.gif" />
							</div>
						</div>
					</div>
					<a href="#issue_screenshot_preview" class="mdl-button mdl-js-button mdl-js-ripple-effect next arrow" role="button">
						<i class="material-icons">&#xe5cc</i>
					</a>
				</div>
				<p class="preview-image-counter text-center">
					<span class="current ap__text"></span> /  <span class="total ap__text"></span>
				</p>
			</div>
		</div>
	</div>
</div>
<div class="modal fade v-center zoomed-image" tabindex="-1" role="dialog" id="attachment_zoom">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header preview-image-header">
				<div class="icon">
					<div class="author_icon" id="attachment_zoom_avatar"></div>
				</div>
				<div class="u-dis-f-c">
					<p id="attachment_zoom_name" class="name"></p>
					<p id="attachment_zoom_date" class="date"></p>
				</div>
				<div class="attachment-preview-btns">
					<a href="#" rel="nofollow" download
						class="mdl-button mdl-js-button mdl-js-ripple-effect ap__btn--primary ap__btn--new ap__btn"
						id="attachment_preview_download">
						<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/line_download_white.svg" alt="Download">
						<span class="ap__text">Download</span>
					</a>
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__btn--secondary ap__btn--new ap__btn hidden"
						id="attachment_preview_delete">
						<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/trash_red.svg" alt="Download" >
					</button>
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__modal-close" data-dismiss="modal">
						<i class="material-icons">close</i>
					</button>
				</div>
			</div>
			<div class="modal-body scroll">
				<div class="u-dis-f-rc box">
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect js-att-button prev arrow">
						<i class="material-icons">&#xe5cb</i>
					</button>
					<div class="preview-image-holder hidden">
						<img src="" alt="Image" id="attachment_zoom_image" class="img-responsive">
					</div>
					<div class="preview-image-holder hidden">
						<video controls src="" id="attachment_zoom_video"></video>
					</div>
					<button class="mdl-button mdl-js-button mdl-js-ripple-effect js-att-button next arrow">
						<i class="material-icons">&#xe5cc</i>
					</button>
				</div>
				<p class="preview-image-counter text-center">
					<span class="current ap__text"></span> /  <span class="total ap__text"></span>
				</p>
			</div>
		</div>
	</div>
</div>
<!-- Show the Issue screenshot tab's images -->
<div class="modal fade v-center zoomed-image zoomed-image--auto-width zoomed-image-player" tabindex="-1" role="dialog" id="issue_flow_preview_modal">
	<div class="modal-dialog" role="document">
		<div class="modal-content">
			<div class="modal-header preview-image-header">
				<div class="icon js-user-image"></div>
				<p class="js-user-image-time zoomed-image-time"></p>
				<button class="mdl-button mdl-js-button mdl-js-ripple-effect ap__modal-close" data-dismiss="modal">
					<i class="material-icons">close</i>
				</button>
			</div>
			<div class="modal-body scroll js-player">
				<div class="box">
					<div id="issue_flow_preview" class="carousel slide sa__carousel carousel-fade" data-ride="carousel">
						<div class="carousel-inner">
							<div class="item active">
								<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/Loader.gif" />
							</div>
						</div>
					</div>
				</div>
				<div class="preview-image-counter text-center">
					<div class="carousel-play carousel-play--blue">
						<a class="left carousel-play__icon--loop" title="Repeat">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/reset.svg" class="white-icon" alt="Repeat">
						</a>
						<a class="left first-slider" href="#" title="First">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/back.svg" class="carousel-play__first__last white-icon" alt="First">
						</a>
						<a class="left" href="#issue_flow_preview" data-slide="prev" title="Prev">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/prev.svg" class="carousel-play__prev__next white-icon" alt="Previous">
						</a>
						<div title="Play/Pause" class="toggle-carousel">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/play.svg" class="carousel-play__icon white-icon" alt="Play">
						</div>
						<a class="right" href="#issue_flow_preview" data-slide="next" title="next">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/forward.svg" class="carousel-play__prev__next white-icon" alt="Next">
						</a>
						<a class="left last-slider" href="#" title="Last">
							<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/next.svg" class="carousel-play__first__last white-icon" alt="Last">
						</a>

						<div class="btn-group dropup">
							<button type="button" class="btn dropdown-toggle u-dis-f-rc" id="play_speed_controll" data-toggle="dropdown"
								aria-haspopup="true" aria-expanded="false">
								<span>1x</span>
							</button>
							<ul class="dropdown-menu play-speed-controller ap__ dropdown-menu">
								<li class="dropdown-header">Playback speed</li>
								<li value="3250">0.2x</li>
								<li value="2500">0.5x</li>
								<li value="1750">0.7x</li>
								<li value="1000">1x</li>
								<li value="750">1.5x</li>
								<li value="500">2x</li>
								<li value="250">3x</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

	<!-- To edit Magic words and Actions for Github settings -->
	<div class="modal fade v-center bug-report__delete-issue" id="edit-status-settings-modal" role="dialog">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-body">
					<div class="row margin-zero u-dis-f-rc">
												<div class="col-xs-4 hidden-xs text-center mim__left">
								<img class="banner" loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_edit_details.svg" alt="Banner">
								<p class="mim__sub-desc mim__sub-desc-first">You can set magic word and actions for workflow to mapping with github.</p>
						</div>
												<div class="col-xs-12 col-sm-8 mim__right">
							<button type="button" data-dismiss="modal" class="mdl-button--icon mdl-button mdl-js-button mdl-js-ripple-effect close-btn close">
								<i class="material-icons">close</i>
							</button>
							<div class="sprint-header">
								<p class="header-text">Github workflow configure</p>
								<p class="header-sub-desc">You can update Github actions and magic words for this status</p>
							</div>
							<div class="sprint-body">
								<form class="" action="" method="post" class="">
									<fieldset class="bug-report__table--slide">
										<div class="github-settings-content">
											<p class="mim__title mw_header">
												<span>Select Action</span>
												<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/info.svg" title="Mapped actions are disabled" class="icon" alt="" data-toggle="tooltip">
											</p>
											<div id="wm_git_actions_list">
																																				<div class="u-dis-f-rc">
													<label class="mapping-show-all-checkbox-container">
														<input class="git-action" type="checkbox" name="git-action" data-action="New Branch">
														<span class="mapping-show-all-checkbox-checkmark"></span>
													</label>
													<span class="ap__text handel-over-flow multi_selection">New Branch</span>
												</div>
																								<div class="u-dis-f-rc">
													<label class="mapping-show-all-checkbox-container">
														<input class="git-action" type="checkbox" name="git-action" data-action="New Pull Request">
														<span class="mapping-show-all-checkbox-checkmark"></span>
													</label>
													<span class="ap__text handel-over-flow multi_selection">New Pull Request</span>
												</div>
																								<div class="u-dis-f-rc">
													<label class="mapping-show-all-checkbox-container">
														<input class="git-action" type="checkbox" name="git-action" data-action="Merge Request">
														<span class="mapping-show-all-checkbox-checkmark"></span>
													</label>
													<span class="ap__text handel-over-flow multi_selection">Merge Request</span>
												</div>
																							</div>
											<p class="mim__title">
												<span>Magic Words</span>
												<img loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/info.svg" data-toggle="tooltip" title="Each status is mapped to unique magic word" class="icon" alt="">
											</p>
											<ul class="list-inline assigned-list ap__tags bug-update__dropdown multi-selection-dropdown" id="cust_multi_select_">
												<div class="dropup dropdown--opt js-dropdown-hidden js-multi-selection-dropdown" data-field-id="" data-type="custom_multi_select">
													<a href="#" class="add-tag-opt js-tooltip" data-action-type="edit">+ Add words
													</a>
													<ul class="dropdown-menu multi-selection-list">
														<i class="material-icons close">close</i>
														<li class="header text-center">Add Magic words</li>
														<hr>
														<div class="add-magic-word-section">
															<ul id="tag_setup_form">
																<li class="input">
																	<textarea name="ws_magic_words" class="ws_magic_words"></textarea>
																	<label class="error hidden ws_magic_words-error" for="ws_magic_words"></label>
																</li>
															</ul>
															<button class="banner_btn mdl-button mdl-js-button mdl-js-ripple-effect  js-new_team__event ap__btn ap__btn--new ap__btn--primary ap__btn--primary-new add-new-magic-word" data-action-type="edit">
																<span class="add-wizard-tag-text">Add</span>
															</button>
														</div>
													</ul>
												</div>
												<!-- Show added options as tags -->
												<div class="multi-selected-list">
												</div>
											</ul>
										</div>
										<div class="update-github-button-div" >
											<button type="button" data-dismiss="modal" class="mdl mdl-button mdl-js-ripple-effect ap__btn ap__btn--secondary ap__btn--new">Cancel</button>
											<button type="button" type="submit" class="mdl-button mdl-js-button mdl-js-ripple-effect ap__btn ap__btn--primary ap__btn--new js-update-status-info" data-update="github-settings" data-actions="" data-color="" data-assignees="" value="">Update</button>
										</div>
									</fieldset>
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!-- Github Integrations steps -->
	<div class="modal fade v-center" role="dialog" tabindex="-1" id="git_integration_steps_modal">
		<div class="modal-dialog">
			<div class="modal-content">
				<div class="modal-body">
					<div class="modal-header u-dis-f-rc">
						<img width="40px" height="40px" loading="lazy" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/githublogo.png" alt="Github">
						<p>Github connection for team</p>
						<button type="button" data-dismiss="modal" class="mdl-button--icon mdl-button mdl-js-button mdl-js-ripple-effect close-btn close">
							<i class="material-icons">close</i>
						</button>
					</div>
					<div class="panel-group gh__connected-steps scroll-thin " id="github_accordion" role="tablist" aria-multiselectable="true">
						<div class="ap__widget panel panel-default">
							<div class="panel-heading" role="tab" id="headingOne">
								<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_icon_step1.svg" alt="Github">
								<div>
									<h4 class="panel-title"><span class="text">Automatically Open Issues</span></h4>
									<div id="open_issues" class="panel-collapse" role="tabpanel">
										<div class="panel-body">
											<p>Your issues in Bugasura will automatically be moved to the <b>OPEN</b> stage as soon as you start the dev on Github. Bugasura will monitor your Github repo for any indication of the issue ID, and once it finds it, it can automatically change the status.
											</p>
										</div>
									</div>
								</div>
								<a data-toggle="collapse" data-parent="#github_accordion" href="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
									<span class="open-collapse">Read More </span><span class="close-collapse">Collapse</span><span class="material-icons">&#xe313</span>
								</a>
							</div>
							<div id="collapseOne" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingOne">
								<div class="collapse-body">
									<div class="illustration">
										<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_step1.svg" alt="Github">
									</div>
									<p>There are 3 places you can include your Issue ID.</p>
									<ul>
										<li>
											<span>a. The BRANCH NAME</span>
											<p>&emsp;- Name your branch with the issue ID eg: <code>B_AN_SN-23_COLOR_SCHEME_CHANGES</code>. Where <code>SN-23</code> is the Issue ID.</p>
										</li>
										<li>
											<span>b. The PULL REQUEST TITLE</span>
											<p>&emsp;- Name your pull request with the issue ID eg: 'Color scheme changes for <code>SN-23</code>'. Where <code>SN-23</code> is the Issue ID.</p>
										</li>
										<li>
											<span>c. The PULL REQUEST DESCRIPTION</span>
											<p>&emsp;When you want to update multiple Issues, you can include the Issue IDS in the pull request description.</p>
											&emsp;<i>eg:</i><br>
											&emsp;&emsp;- <i> Color scheme changes for</i> <code>SN-23</code><br>
											&emsp;&emsp;- <i>UI fixes for</i> <code>SN-12</code><br>
											&emsp;Where <code>SN-23</code> and <code>SN-12</code> are the Issue IDs<br>
										</li>
									</ul>
									<br>
									<p>As soon as Bugasura detects the Issue ID in your repo, the issue(s) will be automatically moved to the Open stage. You can also customize this in the Workflow Section.</p>
									<p class="note"><b>Note:</b> Remember to separate your issue id from the other text with either an <code>'_'</code>, <code>'-'</code> or <code>' '</code>.</p>
								</div>
							</div>
						</div>
						<div class="ap__widget panel panel-default">
							<div class="panel-heading" role="tab" id="headingTwo">
								<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_icon_step2.svg" alt="Github">
								<div>
									<h4 class="panel-title"><span class="text">Automatically Change Issue Status</span></h4>
									<div id="change_status" class="panel-collapse" role="tabpanel">
										<div class="panel-body">
											<p>You can use <b>MAGIC WORD</b> in Github to change the status in Bugasura. There are special words that Bugasura will listen to in your repo. These will indicate to Bugasura that you need the status to be updated.
											</p>
										</div>
									</div>
								</div>
								<a data-toggle="collapse" data-parent="#github_accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
									<span class="open-collapse">Read More </span><span class="close-collapse">Collapse</span><span class="material-icons">&#xe313</span>
								</a>
							</div>
							<div id="collapseTwo" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingTwo">
								<div class="collapse-body">
									<div class="illustration">
										<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_step2.svg" alt="Github">
									</div>
									<p>These magic words can be included in two places.</p>
									<ul>
										<li><span>a. Github Comments</span></li>
										<li><span>b. Github Pull Request Description</span></li>
									</ul>
									<br>
									<p>Examples of Magic words are <i>fixed, fixing, fixes, open, closed, released,</i> etc.<br><br>
										When Bugasura detects these words and the corresponding Issue ID in either the comment or the pull desc, it automatically changes your issue status and updates the comment to the Issue.<br><br>
										<i>eg: Adding a comment</i> "<b>##</b>Fixes<b>##</b> for SN-23" will<br>
										<i>&emsp;a. Change the status</i> of <code>SN-23</code> to InProgress<br>
										<i>&emsp;b. Add a comment in the issue about it</i><br><br>
									</p>
									<p class="note"><b>Note:</b> You can also customize the magic words you want to use for each status change in the Workflow section. Use <b>##</b> to identify magic word as shown in example above.</p>
								</div>
							</div>
						</div>
						<div class="ap__widget panel panel-default">
							<div class="panel-heading" role="tab" id="headingThree">
								<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_icon_step3.svg" alt="Github">
								<div>
									<h4 class="panel-title"><span class="text">Linking your issue to Github</span></h4>
									<div id="link_issues" class="panel-collapse" role="tabpanel">
										<div class="panel-body">
											<p>Whenever Bugasura detects a status change or you mention your issue ID in the Github repo, it automatically adds link back to the issue. This ensures you click and review the changes from your issue itself.
											</p>
										</div>
									</div>
								</div>
								<a data-toggle="collapse" data-parent="#github_accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree"><span class="open-collapse">Read More </span><span class="close-collapse">Collapse</span><span class="material-icons">&#xe313</span>
								</a>
							</div>
							<div id="collapseThree" class="panel-collapse collapse" role="tabpanel" aria-labelledby="headingThree">
								<div class="collapse-body">
									<div class="illustration">
										<img loading="lazy" decoding="async" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/github_integration_step3.svg" alt="Github">
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

<!-- Intro for Left Nav Start -->

<!-- Intro for Left Nav End -->
<script type="text/javascript">
	var introLeftNav = '';

	var emailDomains = '';

	// Create report Variables
	var createReportAppId = '';
	var createReportAppName = '';
	var createReportTestrunId = '';
	var createReportTeamId = '';
	var createReportPlatform = '';
	var createReportPlatformType = '';
	var createReportTestingType = '';
	var is_new_build = 0;
	var currTeamName = ``;
	var currTeamId = '';
	var currProjectImage = '';
	var currProjectAvatarIndex = 0;
	var selectedProjectAvatarTemplate = `<i class="material-icons js-project-icon-selected project-icon-selected">&#xe876</i>`;
	var projectImage = document.getElementById('project_icon_preview_crop'),
	projectImageCropper, projectImageBase64data = '';

	//Time calculation for time spent event
	var startTime; // Store the start time when the page becomes visible
	var modalstartTime;   //For contextual AI modal
	var modaltotalTime=0;
	var integrationPgStartTime;  //for integration page
	var integrationPgtotalTime=0;
	var totalTime = 0; // Total time spent on the page

	window.onload = function (){
		startTime = performance.now(); // Start the timer
		
	}

	// main visibility API function
	// use visibility API to check if current tab is active or not
	var vis = (function(){
		var stateKey,
			eventKey,
			keys = {
					hidden: "visibilitychange",
					webkitHidden: "webkitvisibilitychange",
					mozHidden: "mozvisibilitychange",
					msHidden: "msvisibilitychange"
		};
		for (stateKey in keys) {
			if (stateKey in document) {
				eventKey = keys[stateKey];
				break;
			}
		}
		return function(c) {
			if (c) document.addEventListener(eventKey, c);
			return !document[stateKey];
		}
	})();

	// Visibility change handler
	vis(function() {
	    if (vis()) {
	        if(startTime == 0){
		        startTime = performance.now(); // Start the timer
		        
	        }
	        if(modalstartTime == 0){
		        modalstartTime = performance.now();
		        
		    }
		    if(integrationPgStartTime == 0){
		        integrationPgStartTime = performance.now();
		        
		    }
	    } else {
	        if (startTime) {
	            const currentTime = performance.now();
	            totalTime += currentTime - startTime; // Add time spent to totalTime
	            startTime = 0;
	            
	        }
	        if (modalstartTime) {
	            const currentmodalTime = performance.now();
	            modaltotalTime += currentmodalTime - modalstartTime; // Add time spent to totalTime
	            modalstartTime = 0;
	            
	        }
	        if (integrationPgStartTime) {
	            const currentIntegrationPgTime = performance.now();
	            integrationPgtotalTime += currentIntegrationPgTime - integrationPgStartTime; // Add time spent to totalTime
	            integrationPgStartTime = 0;
	            
	        }
	    }
	});

	// Handle focus and blur events based on browser support
	if (window.addEventListener) {
	    window.addEventListener("focus", function(event) {
	        if(startTime == 0){
		        startTime = performance.now();
		        
		    }
		    if(modalstartTime == 0){
		        modalstartTime = performance.now();
		        
		    }
		    if(integrationPgStartTime == 0){
		        integrationPgStartTime = performance.now();
		        
		    }    
	    }, false);

	    window.addEventListener("blur", function(event) {
	        if (startTime) {
	            const currentTime = performance.now();
	            totalTime += currentTime - startTime;
	            startTime = 0;
	            
	        }
	        if (modalstartTime) {
	            const currentmodalTime = performance.now();
	            modaltotalTime += currentmodalTime - modalstartTime; // Add time spent to totalTime
	            modalstartTime = 0;
	            
	        }
	        if (integrationPgStartTime) {
	            const currentIntegrationPgTime = performance.now();
	            integrationPgtotalTime += currentIntegrationPgTime - integrationPgStartTime; // Add time spent to totalTime
	            integrationPgStartTime = 0;
	            
	        }
	    }, false);
	} else {
	    // Fallback for older browsers
	    window.attachEvent("focus", function(event) {
	        if(startTime == 0){
		        startTime = performance.now();
		        
		    }
		    if(modalstartTime == 0){
		        modalstartTime = performance.now();
		        
		    }
            if(integrationPgStartTime == 0){
		        integrationPgStartTime = performance.now();
		        
		    }
	    });

	    window.attachEvent("blur", function(event) {
	        if (startTime) {
	            const currentTime = performance.now();
	            totalTime += currentTime - startTime;
	            startTime = 0;
	            
	        }
	        if (modalstartTime) {
	            const currentmodalTime = performance.now();
	            modaltotalTime += currentmodalTime - modalstartTime; // Add time spent to totalTime
	            modalstartTime = 0;
	            
	        }
	        if (integrationPgStartTime) {
	            const currentIntegrationPgTime = performance.now();
	            integrationPgtotalTime += currentIntegrationPgTime - integrationPgStartTime; // Add time spent to totalTime
	            integrationPgStartTime = 0;
	            
	        }
	    });
	}

	function mixPanelTimeSpent(eventProperty){
        
        //Calculate total time spent on current page
	    const currentTime = performance.now(); //Performance.now is a web api geting time in millisec
        totalTime += currentTime - startTime;

        var totalTime_Sec = totalTime /1000;

        //Add calculated time in eventProperty
        eventProperty = Object.assign(eventProperty,{"Time Spent" : totalTime_Sec});

        //Mixpanel tracking for Time spent event
		if ( typeof registerMIXPEvent === 'function' )registerMIXPEvent("Time Spent","",eventProperty);

	}


	$(document).ready(function() {

		
		
		$('#create-sprint-report').prop('disabled', false);
		isModalOpen( '#issue_flow_preview_modal, #issue_comment_image_preview_modal, #issue_screenshot_preview_modal' );

				// Hidding bug report popup on pressing esc key
		$(document).keydown(function(event) {
			if ( event.keyCode == 27 ) {
				$("#sprint-create-form").modal('hide');
			}
		});

		$(document).on('click', "[data-error-type='appsumo-plan-invite']", function(e) {
			toastrMsg("Kindly contact support@bugasura.io to invite more team members to your team.", 'error', true);
		});

		/*-------------------- Additional Validator - START -----------------------*/
		// Custome email validtion
		jQuery.validator.addMethod("customEmail",
		 function(value, element) {
			return emailValidation( value );
		}, 'Oops, doesn’t look like work email!');

		// Custom email validtion
		jQuery.validator.addMethod("validateEmail",
		 function(value, element) {
			return validateEmail( value );
		}, 'Please provide valid Email-Id');

		// specialCharsSpace validator
		jQuery.validator.addMethod("specialCharsSpaceBuilds", function( value, element ) {
				var regex = new RegExp("^[a-zA-Z0-9()._-\\s]+$");
				var key = value;
				if (!regex.test(key) && value != '') {
				   return false;
				}
				return true;
		}, "Please use only alphanumeric or alphabetic characters.");


		jQuery.validator.addMethod("firstCharSpace", function(value, element) {
			if (value.substr(0,1) == " ") {
				return false;
			}
			return true;
		}, "First character cannot be space");

		jQuery.validator.addMethod("firstCharAlphanumeric", function (value, element) {
			var regex = new RegExp("^[a-zA-Z0-9]{1}");
			var key = value;
			if (!regex.test(key) && value != '') {
				return false;
			}
			return true;
		}, "First character should be alphanumeric character");

		// specialCharsSpaceColon Validator
		jQuery.validator.addMethod("specialCharsSpaceColon", function( value, element ) {
			var regex = new RegExp("^[a-zA-Z0-9._:-\\s]+$");
			var key = value;
			if (!regex.test(key) && value != '') {
			   return false;
			}
			return true;
		}, "Please use only alphanumeric or alphabetic characters.");

		// Allow only first alpha character Validator
		jQuery.validator.addMethod("firstAlpha", function( value, element ) {
			var regex = new RegExp('^[a-zA-Z]{1}[ A-Za-z0-9_-]*$');
			var key = value;
			if (!regex.test(key) && value != '') {
				return false;
			}
			return true;
		}, "First character should be alphabetic.");

		jQuery.validator.addMethod("alphanumericAllowed", function(value, element) {
			return this.optional(element) || /^[a-zA-Z0-9_-\s]{1,}$/i.test(value);
		}, `Cannot have special characters except "_" and "-".`);

		jQuery.validator.addMethod("customFieldsSpecialChars", function(value, element) {
			return this.optional(element) || /^[a-zA-Z0-9_-\s!@#$%^&*()+;:\'\",.\/<>?\\]{1,}$/i.test(value);
		}, `Cannot have special characters except underscore, hyphen, exclamation mark, at, hash, dollar, percentage, caret, asterisk, parenthesis, colon, semi-colon, apostrophe, quote, comma, period, slash, angle brackets, question mark, plus sign and space.`);

		// specialCharsSpaceColonApostrophe Validator
		jQuery.validator.addMethod("specialCharsSpaceColonApostrophe", function( value, element ) {
			var regex = new RegExp("^[a-zA-Z0-9._:-\\s\']+$");
			var key = value;
			if (!regex.test(key) && value != '') {
			   return false;
			}
			return true;
		}, "Please use only alphanumeric characters");

		$.validator.addMethod('validUrl', function(value, element) {
			var url = $.validator.methods.url.bind(this);
			return url(value, element) || url('http://' + value, element);
		}, 'Please enter a valid URL');
		jQuery.validator.addMethod(
			"multiemail",
			function (value, element) {
				if (this.optional(element)) // return true on optional element
					return true;
				// var emails = value.split(/[;,]+/); // split element by , and ; spance
				var emails = value.split(','); // split element by , and ; spance
				var valid = true;
				var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,100}$/i);
				for (var i in emails) {
					value = emails[i];
					valid = valid && pattern.test($.trim(value));
				}
				return valid;
			},

			"Please enter valid email id separated comma"
		);

		$.validator.addMethod("notOnlyZero", function (value, element, param) {
			if ( $.isNumeric( value )  )
				return this.optional(element) || parseFloat(value) > 0;

			return true;
		});

		// Custome password validtion check for empty space
		jQuery.validator.addMethod("customPassword",
		 function(value, element) {
			return ( $.trim( value ) == '' ) ? false : true;
		}, 'Password should be atleast 5 characters.');

		/*-------------------- Additional Validator - END -----------------------*/
		
		$(document).mouseup(function(e) {
			var container = $("#sprint-create-form .modal-content");
			// if the target of the click isn't the container nor a descendant of the container
			if ( ( !container.is(e.target) && container.has(e.target).length === 0 ) ){
				$("#sprint-create-form").modal('hide');
			}
		});

		$(".ap__siderbar--toggle").on('click',function () {
			if ($("body").hasClass("minimized")) {
				$(this).removeClass('minimized');
				$("body").removeClass("minimized");
				document.cookie = "minimized=0; expires=Sun, 15 Jan 2023 12:00:00 UTC; path=/";
			} else {
				$("body").addClass("minimized");
				$(this).addClass('minimized');
				document.cookie = "minimized=1; expires=Sun, 15 Jan 2023 12:00:00 UTC; path=/";
			}
		});
		// Validate emails, error on entering any disposable email ids
		function emailValidation( email ) {
			if ( !emailDomains ) emailDomains = $.trim($('#disposal_emails').text().replace(/(\r\n|\n|\r)/gm,"")).split(',');
			var n = email.indexOf("@");
			var emailDomain = email.substring(n+1).toLowerCase();
			return $.inArray( emailDomain, emailDomains ) === -1;
		}
		function validateEmail(email) {
			const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			return re.test(String(email).toLowerCase());
		}

		$('#up-btn').on('click',function(e){
			e.preventDefault();
		});

		


		
		
			
			/* ---------- JS Script for Team User Invite - END ---------- */

			/* ---------- JS Script for New Feature Modal - START ---------- */

			// Function run after hiding new feature popup modal
			$("#new_features_popup").on('hidden.bs.modal',function() {
				$('.ap__siderbar-compact').css("z-index",1062);
				$('.ap__siderbar-compact li.not-active').addClass('active').removeClass('not-active');
				$('#whats_new').parent().removeClass('active');
			});

			// Function run before opening new feature popup modal
			$('#whats_new').on('click',function(e) {
				if ( $(this).parent().hasClass('active') ) return;
				$('.ap__siderbar-compact').css("z-index",100001);
				$('.ap__siderbar-compact li.active').addClass('not-active').removeClass('active');
				$(this).parent().addClass('active');

				$('#new_features_popup').modal('show');
				if ($('#whats_new').attr('data-is-loaded')) return;

				$.get('https://my.bugasura.io/releaseNotes/getPublishedReleaseNotes',{},function(response) {
					$('#new_features_popup .modal-body').empty().removeClass('u-dis-f-rc').append(response);
					$('#whats_new .ap__siderbar-compact-dot').remove();
				}, 'html');

				//Mixpanel Tracking for new feature popup
				if ( typeof registerMIXPEvent === 'function' )registerMIXPEvent('Viewed whats new section');
 
			});

			/* ---------- JS Script for New Feature Modal - END ---------- */

			// Function run before opening new feature popup modal
			$('#intro_help').on('click',function(e) {
				restartIntroIntroStep();
			});

		
		/* ------------ AI Modal ajax call - START  ---------------- */
			$('.js-ai-link').on('click',function(e) {
				getAIContextModal();
			});
		/* ------------ AI Modal ajax call - END  ---------------- */

				var distanceMobTop = 0;
		if ( $('.js-window-mob-top-element').length ) {
			var distanceMobTop = $('.js-window-mob-top-element').offset().top;
			// On scroll check if it's reached to window top.
			// If it's reached top make it sticky on top else place it normal.
			$(window).scroll(function() {

				if ( $(window).scrollTop() >=  (distanceMobTop - 85) ){
					$('.ap__nav-mobile.js-window-mob-top-element').addClass('affix');
					$('.issues-operations').addClass('affix');
				}
				if ( $('.js-window-mob-top-element').offset().top <= distanceMobTop ){
					$('.ap__nav-mobile.js-window-mob-top-element').removeClass('affix');
					$('.issues-operations').removeClass('affix');
				}

			});
		}

		// $('.js-option-edit').on('input change', function() {
		// }).blur(function() {
		// 	$('.js-project-name').css('color', '');
		// 	if ( $(this).val() == '' ) {
		// 		_this.teamName = 'My Team';
		// 		$(this).addClass('default-color-text');
		// 	}
		// 	$(this).val(_this.teamName).trigger('change');
		// 	if(!$(this).valid()){
		// 		$('.js-go-to-slide.next').addClass('disabled').removeClass('in');
		// 	}
		// });

				
		// Click event for Product Hunt page trigger
		$(document).on('click', '#support_launch_btn', function(e){
			e.preventDefault();
			var url = $(this).attr('href');
			$("#product_hunt_modal").modal('hide');
			window.open(url, '_blank');
		});
				$(document).on('click', '.js-reaction[data-testresults_id]>img', function(e) {
			e.preventDefault();
			e.stopPropagation();
			if ( $(this).parents('.js-disabled').length ) {
				return;
			}
						var parentElem = $(this).parents('.js-reaction');
			var isIssueReaction = 1;
			var testResultsId = parentElem.data('testresults_id');
			var commentId = '';
			if ( parentElem.attr('data-comment_id') != '' )
				commentId = parentElem.attr('data-comment_id');
			if ( parentElem.hasClass('js-comment-react') || commentId != '' ) {
				isIssueReaction = 0;
			}
			var isLiked = parentElem.hasClass('like')? 1: 0;
			var mainParentElem = parentElem.parent();
			var likeCount = mainParentElem.find('.js-reaction.like').data('count') ? mainParentElem.find('.js-reaction.like').data('count'): 0;
			var dislikeCount = mainParentElem.find('.js-reaction.dislike').data('count') ? mainParentElem.find('.js-reaction.dislike').data('count'): 0;
			$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).addClass('prev-active');
			mainParentElem.addClass('js-disabled');
			if ( parentElem.hasClass('active') ) {
				if ( isLiked ) {
					likeCount = likeCount > 0? likeCount-1: 0;
				} else {
					dislikeCount = dislikeCount > 0? dislikeCount-1: 0;
				}
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).removeClass('active');
				updateReactionCount( testResultsId, commentId, likeCount, dislikeCount );
				removeReaction( testResultsId, commentId, isIssueReaction, parentElem);
			} else {
				if ( isLiked ) {
					likeCount++;
					if ( mainParentElem.find('.js-reaction.dislike').hasClass('active') ) {
						dislikeCount = dislikeCount > 0? dislikeCount-1: 0;
					}
				} else {
					dislikeCount++;
					if ( mainParentElem.find('.js-reaction.like').hasClass('active') ) {
						likeCount = likeCount > 0? likeCount-1: 0;
					}
				}
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).removeClass('active');
				var className = isLiked ? '.like' : '.dislike';
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}']${className}`).addClass('active');
				updateReactionCount( testResultsId, commentId, likeCount, dislikeCount );
				addUpdateReaction( testResultsId, commentId, isLiked, isIssueReaction, parentElem);
			}
		});

	});
	// document.read() END

	function isValidOptionValue( optionValue, inputElem, prevValue ) {
		optionValue = optionValue.trim();
		var optionLength = optionValue.length;
		inputElem.removeClass('error');
		$(".option-error .error").addClass('hidden').removeAttr('style');
		if ( optionLength <= 0 ) {
			inputElem.addClass('error');
			$(".option-error .error").text('Please enter the option value.').removeClass('hidden');
			return false;
		} else if ( optionLength > 50 ) {
			inputElem.addClass('error');
			$(".option-error .error").text('Please enter less than 50 character.').removeClass('hidden');
			return false;
		} else if ( !(/^[a-zA-Z0-9_-\s!@#$%^&*()+;:\'\",.\/<>?\\]{1,}$/i).test(optionValue) ) {
			inputElem.addClass('error');
			$(".option-error .error").text(`Cannot have special characters except underscore, hyphen, exclamation mark, at, hash, dollar, percentage, caret, asterisk, parenthesis, colon, semi-colon, apostrophe, quote, comma, period, slash, angle brackets, question mark, plus sign and space.`).removeClass('hidden');
			return false;
		} else if ( prevValue != optionValue ) {
			var isExist = false;
			$('#custom_dropdown_items .scroll li').each(function(){
				optValue = $(this).attr('data-item');
				if ( optionValue == optValue ) {
					isExist = true;
					return false;
				}
			});
			if ( isExist ) {
				inputElem.addClass('error');
				$(".option-error .error").text('This option already exist.').removeClass('hidden');
				return false;
			}
		}
		return true;
	}

	function addNewItem(ps_item, list_count){
		var fieldType = $("#ps_field_type").val();
		var fieldValue = `<span class="ap__text handel-over-flow js-edit-status-details">${ps_item}</span>`;
		var multiSelectionValue = '';
		if ( fieldType == 'single_selection') {
			fieldValue = `<div class="u-dis-f-rc"><label class="js-bug-report-syn-type mdl-radio mdl-js-radio mdl-js-ripple-effect">
								<input type="radio" class="mdl-radio__button" name="options" value="${ps_item}">
							</label>
							<span class="ap__text handel-over-flow single_selection js-edit-status-details">${ps_item}</span>
							</div>`;
		} else if ( fieldType == 'multi_selection' ) {
			fieldValue = `<div class="u-dis-f-rc"><label class="mapping-show-all-checkbox-container">
								<input type="checkbox" name="mapping-show-all">
								<span class="mapping-show-all-checkbox-checkmark"></span>
							</label>
							<span class="ap__text handel-over-flow multi_selection js-edit-status-details">${ps_item}</span></div>`;
			multiSelectionValue = `<li><span class="ap__text handel-over-flow multi_selection">${ps_item}</span> <i class="material-icons">close</i></li>`;
		}

		var addNewOptionTemplate =`<li class="list dragable" data-item="${ps_item}">
											<div class="option-preview">
												<img class="ps__item-drag-icon" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/icons/drag_gray.svg" alt="Icon">
												${fieldValue}
												<div class="status-preview-opt">
													<img class="ps__item-delete" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/img/delete_option_icon.svg" alt="Icon">
												</div>
											</div>
											<div class="option-edit hidden">
												<div class="option-edit-section">
													<input class="js-option-edit" type="text" value="${ps_item}" maxlength="51" />
													<div class="option-edit-btns">
														<span class="ps__edit-save"><i class="material-icons tick">done</i></span>
														<span class="ps__edit-cancel"><i class="material-icons close">close</i></span>
													</div>
												</div>
											</div>
										</li>`;
		$("#custom_dropdown_items .scroll").append(addNewOptionTemplate);
		if ( fieldType == 'dropdown') {
			var addNewDropdownOptionTemplate =`<li>
												<a href="javascript:void(0);" class="js-dropdown-select js-section-select" role="button">${ps_item}</a>
											</li>`;
			$("#ps_dropdown .dropdown-menu").append(addNewDropdownOptionTemplate);
			$("#ps_dropdown .ap__btn .ap__text").text($('#custom_dropdown_items .scroll li.list').first().attr('data-item'));
		} else if ( fieldType == 'single_selection' ) {
			$("#ps_single_selection").append(fieldValue);

			setTimeout(function() {
				$("#ps_single_selection div").first().find('label').addClass('is-checked');
				$("#ps_single_selection div label").addClass('disable');
			},100);

		} else if ( fieldType == 'multi_selection' ) {
			$("#ps_multi_selection ul").append(multiSelectionValue);

		}
		componentHandler.upgradeDom('MaterialRadio');
	}

	function updateOptionsList(){
		var addNewDropdownOptionTemplate = '', ps_item = '', list_count = 0, multiSelectionValue = '';
		var fieldType = $("#ps_field_type").val();

		$('#custom_dropdown_items .scroll li').each(function(){
			ps_item = $(this).attr('data-item');
			list_count++;
			if ( fieldType == 'dropdown') {
				addNewDropdownOptionTemplate +=`<li>
												<a href="javascript:void(0);" class="js-dropdown-select js-section-select" role="button">${ps_item}</a>
											</li>`;
			} else if ( fieldType == 'single_selection' ) {
				addNewDropdownOptionTemplate +=`<div class="u-dis-f-rc"><label class="js-bug-report-syn-type mdl-radio mdl-js-radio mdl-js-ripple-effect">
							<input type="radio" class="mdl-radio__button js-deployment_type" name="options" value="${ps_item}">
						</label>
						<span class="ap__text handel-over-flow single_selection">${ps_item}</span>
						</div>`;
			} else if ( fieldType == 'multi_selection' ) {
				addNewDropdownOptionTemplate +=`<div class="u-dis-f-rc"><label class="mapping-show-all-checkbox-container">
							<input type="checkbox" name="mapping-show-all">
							<span class="mapping-show-all-checkbox-checkmark"></span>
						</label>
						<span class="ap__text handel-over-flow multi_selection">${ps_item}</span></div>`;
				multiSelectionValue += `<li><span class="ap__text handel-over-flow multi_selection">${ps_item}</span> <i class="material-icons">close</i></li>`;
			}

		});
		if ( fieldType == 'dropdown') {
			$("#ps_dropdown .dropdown-menu").empty().append(addNewDropdownOptionTemplate);
			$("#ps_dropdown .ap__btn .ap__text").text($('#custom_dropdown_items .scroll li.list').first().attr('data-item'));
		} else if ( fieldType == 'single_selection' ) {
			$("#ps_single_selection").empty().append(addNewDropdownOptionTemplate);
			componentHandler.upgradeDom('MaterialRadio');
			$("#ps_single_selection div").first().find('label').addClass('is-checked');
			$("#ps_single_selection div label").addClass('disable');
		} else if ( fieldType == 'multi_selection' ) {
			$('#ps_multi_selection ul').empty();
			$("#ps_multi_selection ul").append(multiSelectionValue);
		}
	}

	
	function getAIContextModal() {
		appId = ``;
		var teamId = currTeamId;
		// Check if the modal exits and then load
		$.get('https://my.bugasura.io//modal/getProjectCommonModals',{
			appId : appId,
			teamId : teamId,
			teamName : currTeamName,
			modalName : 'ai_context_modal',
			mode : 'html'
		}, function (response) {
			$("#project_contextual_ai_modal").empty().append(response);
			$('#contextual_ai_modal').modal('show');
			componentHandler.upgradeAllRegistered()
		});
	}

	function isModalOpen( taget ) {
		// If there two modal are showm.
		// On dismissing/closing one modal will enable the body scroll.
		// To avoid this check if modal-backdrop is there in body then add modal-open class to body tag.
		taget.split(',').forEach(function(value, index) {
			$(value).on('hidden.bs.modal',function() {
				if ( $('body .modal-backdrop.fade.in').length !== 0) $('body').addClass('modal-open');
			});
		})

	}

	/********************** Bugasura icon loading functions *************************/

	function showLoaderTo(parent) {
		const loader = `<div class='show-loader' id="loading_${parent}"><div class="yc-cube-grid">
			<div class="yc-cube yc-cube1"></div>
			<div class="yc-cube yc-cube2"></div>
			<div class="yc-cube yc-cube3"></div>
			<div class="yc-cube yc-cube4"></div>
			<div class="yc-cube yc-cube5"></div>
			<div class="yc-cube yc-cube6"></div>
			<div class="yc-cube yc-cube7"></div>
			<div class="yc-cube yc-cube8"></div>
			<div class="yc-cube yc-cube9"></div>
		</div></div>`
		$(parent).css('overflow', 'hidden');
		$(parent).append(loader);
	}

	/********************** Bugasura icon loading functions end *************************/

	function showToaster() {
		$('#toast-container .toast').css('opacity','0.8');
		setTimeout(function(){ $('#toast-container').fadeOut();}, 8000);
	}

	function showToasterShort() {
		$('#toast-container .toast').css('opacity','0.8');
		setTimeout(function(){ $('#toast-container').fadeOut();}, 3000);
	}

			/********************** Share report model functions *************************/

		function showShareReportModel( buildId, testrunId, reportId, hash ) {

			$('.shareReportbody #share_report_form').validate().resetForm();
			// Input value field reset
			$('.shareReportbody #share_report_form')[0].reset();
			// Set default value for form
			var hashUrl = "https://my.bugasura.io/"+"testReports/"+hash+"/"+reportId;
			// if ( response.buildHashValue ) {
			// 	var appId = response.appId;
			// 	hash = "https://my.bugasura.io/"+"dashboard/"+appId+"/"+response.buildHashValue;
			// }
			var shareFrom= "piyushwaghmarehere@gmail.com";
			var userDesignation = "";
			// var shareBody= "Hi,\n\nI have tested  using the Bugasura Platform and wanted to share the test report with you.\n\n"+hashUrl+"\n\n\nWould love to hear your feedback!\n\nRegards,\nPiyush Waghmare";
			// if ( userDesignation == 'DESIGNER' ) {
			// 	shareBody= "Hi,\n\nI have design reviewed  using the Bugasura Platform and wanted to share the review report with you.\n\n"+hashUrl+"\n\n\nWould love to hear your feedback!\n\nRegards,\nPiyush Waghmare";
			// }

						$('.reportShareablelink').val('');
			$('.reportShareablelink').val(hashUrl);
			$('#shareFrom').val(shareFrom);
			//$('#shareBody').val(shareBody);
			$('#userName').val( "Piyush Waghmare");
			$('#report_id').val(reportId);
			$('#build_id').val(buildId);
			$('#hash_value').val(hash);
			$('#share_submit').text('Send Link');
			$('#shareTo').tagsinput('removeAll');
			$('.share-receipent .bootstrap-tagsinput input').attr('placeholder',"(Max 10 Email IDs)");
			$('#shareReportDialog').modal('show');
		}

		function testReportShare ( testrunID, buildId = '', appId = '' ) {
			// Ajax Call
			$.post('https://my.bugasura.io/testReports/shareToggle',{
				testrun_id	: testrunID,
				buildId		: buildId,
				appId		: appId
			}, shareToggleCallBack,'json');
		}
		function shareToggleCallBack ( response ) {
			$('#toast-container').remove();
			if (response.status == 'ERROR') {
				toastr.error(response.message);
			} else {
				// )Validation error message reset
				$('.shareReportbody #share_report_form').validate().resetForm();
				// Input value field reset
				$('.shareReportbody #share_report_form')[0].reset();
				// Set default value for form
				var hash = "https://my.bugasura.io/"+"testReports/"+response.hash+"";
				var appId = ''
				if ( response.buildHashValue ) {
					appId = response.appId;
					hash = "https://my.bugasura.io/"+"dashboard/"+appId+"/"+response.buildHashValue;
				}

				buildId = _SESSION['buildId']

				var shareFrom= "piyushwaghmarehere@gmail.com";
			//	var shareBody= "Hi,\n\nI have tested  using the Bugasura Platform and wanted to share the test report with you.\n\n"+hash+"\n\n\nWould love to hear your feedback!\n\nRegards,\nPiyush Waghmare";
				$('.reportShareablelink').val(hash);
				$('#shareFrom').val(shareFrom);
				$("#build_id").val(buildId);
				$('#build_hash_value').val(hash);
				$('#userName').val( "Piyush Waghmare");
				$('#share_submit').text('Send Link');
				$('#shareTo').tagsinput('removeAll');
				$('.share-receipent .bootstrap-tagsinput input').attr('placeholder',"(Max 10 Email IDs)");
				$('#shareReportDialog').modal('show');
			}
			showToaster();
		}

		function shareMailSend() {
			$('#share_submit').text('Please Wait...');
			$('#shareReportDialog').addClass("disable");
			var mailContent = $('#share_report_form #shareBody').val().replace(/\n/g, "<br />");
			var shareTo = $("#share_report_form #shareTo").val();
			var shareablelink = $('#share_report_form .reportShareablelink').val();
			var reportId = $('#share_report_form #report_id').val();
			var build_id = $('#share_report_form #build_id').val();
			var hashValue = $('#share_report_form #hash_value').val();
			var buildHashValue = $('#share_report_form #build_hash_value').val();
			var userName = ""+$('#share_report_form #userName').val()+"";
			var shareToArr = shareTo.split(",");
			var isSharedReport = 0;
			var publicProjectLink = '';
			var publicReportName = '';
			
			
			$.post('https://my.bugasura.io/testReports/shareReportEmail',{
				share_body_content : mailContent,
				share_to : shareTo,
				report_id : reportId,
				build_id : build_id,
				user_name : userName,
				report_link : shareablelink,
				is_shared_report : isSharedReport,
				hash_value : hashValue,
				build_hash_value : buildHashValue,
				publicProjectLink : publicProjectLink,
				publicReportName : publicReportName
			},shareMailCallback,'json');
		}

		function shareMailCallback( response ) {
			if ( response.status == 'OK' ){
				toastr.success( response.message );
				$('#shareReportDialog').modal('hide');
				var shareTo = $("#share_report_form #shareTo").val();
				// validation error message reset
				$('.shareReportbody #share_report_form').validate().resetForm();
				// input value field reset
				$('.shareReportbody #share_report_form')[0].reset();
				$('.share-receipent .bootstrap-tagsinput input').removeClass('margin-width');
				$('#shareTo').val("");
			}
			else{
				toastr.error( response.message );
				$('#share_submit').text('Send Link');
			}
			showToaster();
			$('#shareReportDialog').removeClass("disable");
		}
		/********************** Share report model functions END *************************/
	
	// The below sprint-create-form model is not required for any other page except report list
	
	function getNewFeaturesReleased() {
		$.get('https://my.bugasura.io/releaseNotes/getPublishedReleaseNotes',{
			'isOnlyFeatures' : 1
		},function(response) {
			$('#new_features_released_modal').empty().append(response);

			//Mixpanel tracking for Viewed new feature popup
		    if ( typeof registerMIXPEvent === 'function' )registerMIXPEvent('Viewed new feature popup');
		}, 'html');
	}

	// Function to get the current date time in a Format
	function formattedMoment() {
		var thisMoment = new Date();
		var formattedDate = thisMoment.toString().split(" ");
		var hours = thisMoment.getHours();
		var minutes = thisMoment.getMinutes();
		var ampm = hours >=12 ? 'pm' : 'am';
		hours = hours % 12;
		hours = hours ? hours : 12;
		minutes = minutes < 10 ? '0' + minutes : minutes;
		var formattedTime = hours + ':' + minutes + ' ' + ampm;
		return formattedDate[2] + nth( thisMoment.getDate() ) + " " + formattedDate[1] + " " + formattedTime;
	}

	function resetIntroIntroStep() {
		$.post('https://my.bugasura.io/account/updateIntroStep',{
			resetIntro : 'reset'
		},function(response){
			if( response.status == "OK") {
				if ( response.introSettings.isReRunHelpIntro == 0 ) {
					runHelpRerunIntro(response.introSettings);
				}

				//Mixpanel tracking for skipped tour
				if ( typeof registerMIXPEvent === 'function' )registerMIXPEvent("Skipped tour");
				console.log(`The intro step details is updated `);
			} else {
				console.log(`Error while updating intro step details`);
			}
		},'json');

	}

	function restartIntroIntroStep() {
		console.log("inside restartIntroIntroStep");
		//class body
		$.post('https://my.bugasura.io/account/updateIntroStep',{
			resetIntro : 'restart'
		},function(response){
			if( response.status == "OK") {

				reRunIntroStep(response.introSettings );
			} else {
				console.log(`Error while updating intro step details`);
			}
		},'json');
	}

	var introTeamPage_Rerun = '';
	var introProjectPage_leftNav_Rerun = '';
	var introIssuePage_Rerun = '';
	function reRunIntroStep( response ){
		console.log("Repsode",response);
		if ( $('body.goManageTeams').length && $(".app__teams-section.team-member__list a .app__team").length ){
			if (!$('template#manage_team_intro').length)
				$('body').append(`<template id="manage_team_intro">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 25rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.manage_team_intro.intro_image}.svg" alt="Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.manage_team_intro.title}</p>
												<p class="descritpion">${response.manage_team_intro.description}</p>
											</div>
										</div>
									</template>`);


			introTeamPage_Rerun = introJs();
			introTeamPage_Rerun.setOptions({
				nextLabel: "Next",
				skipLabel: "Don’t show this again",
				showBullets:false,
				overlayOpacity:1,
				hidePrev:true,
				disableInteraction:true,
				exitOnOverlayClick: false,
				keyboardNavigation:false,
				tooltipClass: 'ap__intro',
				steps:[{
					name: "manage_team_intro",
					position: 'right-middle',
					element: $('.app__team').first()[0],
					intro:$('#manage_team_intro').html()
				}]
			});
			introTeamPage_Rerun.onchange(function(targetElement) {
				updateIntroStepRerun(this._introItems[this._currentStep].name);
				isShowManageTeamIntro = 0;
			});

			introTeamPage_Rerun.oncomplete(function(css) {
				$('body').removeClass('hide-intro-overflow');
			});

			introTeamPage_Rerun.onexit(function(css) {
				$('body').removeClass('hide-intro-overflow');
			});
			introTeamPage_Rerun.onskip(function(css) {
				$('body').removeClass('hide-intro-overflow');
				resetIntroIntroStep();
			});
			introTeamPage_Rerun.start();
		}

		if ( $('body.getApps').length ){
			if (!$('template#manage_project_intro').length && $(".answer-dashboard .answer__reports.active .apps_block__js").length )
				$('body').append(`<template id="manage_project_intro">
									<div class="intro-box">
										<div class="intro__head">
											<button type="button" class="mdl-button--icon mdl-button mdl-js-button mdl-js-ripple-effect close-intro-btn" aria-label="Close">
												<i class="material-icons">close</i>
											</button>
											<img class="img-responsive" style="width: 28rem; margin-bottom: -1.5rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.manage_project_intro.intro_image}.svg" alt="Intro">
										</div>
										<div class="intro__body">
											<p class="title">${response.manage_project_intro.title}</p>
											<p class="descritpion">${response.manage_project_intro.description}</p>
										</div>
									</div>
								</template>`);
			if (!$('template#create_project_intro').length && !$(".answer-dashboard .answer__reports.active .apps_block__js").length )
				$('body').append(`<template id="create_project_intro">
									<div class="intro-box">
										<div class="intro__head">
											<button type="button" class="mdl-button--icon mdl-button mdl-js-button mdl-js-ripple-effect close-intro-btn" aria-label="Close">
												<i class="material-icons">close</i>
											</button>
											<img class="img-responsive" style="width: 29rem; margin-bottom: -1.5rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.create_project_intro.intro_image}.svg" alt="Intro">
										</div>
										<div class="intro__body">
											<p class="title">${response.create_project_intro.title}</p>
											<p class="descritpion">${response.create_project_intro.description}</p>
										</div>
									</div>
								</template>`);

			if (!$('template#leftnav_projects').length)
				$('body').append(`<template id="leftnav_projects">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 28rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_projects_intro.intro_image}.svg" alt="Project Page">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_projects_intro.title}</p>
												<p class="descritpion">${response.leftnav_projects_intro.description}</p>
											</div>
										</div>
									</template>`);

			if (!$('template#leftnav_my_dashboard').length)
				$('body').append(`<template id="leftnav_my_dashboard">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 26rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_my_dashboard_intro.intro_image}.svg" alt="Add Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_my_dashboard_intro.title}</p>
												<p class="descritpion">${response.leftnav_my_dashboard_intro.description}</p>
											</div>
										</div>
									</template>`);
			if (!$('template#leftnav_wizard').length)
				$('body').append(`<template id="leftnav_wizard">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 24rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_wizard_intro.intro_image}.svg" alt="Add Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_wizard_intro.title}</p>
												<p class="descritpion">${response.leftnav_wizard_intro.description}</p>
											</div>
										</div>
									</template>`);
			if (!$('template#leftnav_release_feature').length)
				$('body').append(`<template id="leftnav_release_feature">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 25rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_release_feature_intro.intro_image}.svg" alt="Add Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_release_feature_intro.title}</p>
												<p class="descritpion">${response.leftnav_release_feature_intro.description}</p>
											</div>
										</div>
									</template>`);
			if (!$('template#leftnav_settings').length)
				$('body').append(`<template id="leftnav_settings">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 24rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_settings_intro.intro_image}.svg" alt="Add Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_settings_intro.title}</p>
												<p class="descritpion">${response.leftnav_settings_intro.description}</p>
											</div>
										</div>
									</template>`);
			if (!$('template#leftnav_user_profile').length)
				$('body').append(`<template id="leftnav_user_profile">
										<div class="intro-box">
											<div class="intro__head">
												<img class="img-responsive" style="width: 21rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_user_profile_intro.intro_image}.svg" alt="Add Issue">
											</div>
											<div class="intro__body">
												<p class="title">${response.leftnav_user_profile_intro.title}</p>
												<p class="descritpion">${response.leftnav_user_profile_intro.description}</p>
											</div>
										</div>
									</template>`);

			introProjectPage_leftNav_Rerun = introJs();
			introProjectPage_leftNav_Rerun.setOptions({
				nextLabel: "Next",
				skipLabel: "Don’t show this again",
				doneLabel: "Explore",
				showBullets:false,
				overlayOpacity:1,
				hidePrev:true,
				disableInteraction:true,
				exitOnOverlayClick: false,
				keyboardNavigation:false,
				helperElementPadding: 5,
				tooltipClass: 'ap__intro',
				steps:[]
			});
			if ( $(".answer-dashboard .answer__reports.active .apps_block__js").length ){
				introProjectPage_leftNav_Rerun.addSteps([{
					name: "manage_project_intro",
					position: 'project-intro-position',
					element: $('.apps_block__js').first()[0],
					intro: $('#manage_project_intro').html()
				}]);
			}
			introProjectPage_leftNav_Rerun.addSteps([{
				name: "leftnav_projects_intro",
				position: 'leftnav-projects',
				element: $('.project-btn')[0],
				intro:$('#leftnav_projects').html()
			}]);
			introProjectPage_leftNav_Rerun.addSteps([{
				name: "leftnav_my_dashboard_intro",
				position: "leftnav-my-dashboard",
				element: $('.my-dashboard-btn')[0],
				intro:$('#leftnav_my_dashboard').html()
			}]);
			introProjectPage_leftNav_Rerun.addSteps([{
				name: "leftnav_release_feature_intro",
				position: "leftnav-release-feature",
				element: $('#whats_new')[0],
				intro:$('#leftnav_release_feature').html()
			}]);
			introProjectPage_leftNav_Rerun.addSteps([{
				name: "leftnav_settings_intro",
				position: "leftnav-settings",
				element: $('.leftnav-settings-btn')[0],
				intro:$('#leftnav_settings').html()
			}]);
			introProjectPage_leftNav_Rerun.addSteps([{
				name: "leftnav_user_profile_intro",
				position: "leftnav-user-profile",
				element: $('.leftnav-user-profile')[0],
				intro:$('#leftnav_user_profile').html()
			}]);

			introProjectPage_leftNav_Rerun.onchange(function(targetElement) {
				updateIntroStepRerun(this._introItems[this._currentStep].name);
			});

			introProjectPage_leftNav_Rerun.oncomplete(function(css) {
				$('body').removeClass('hide-intro-overflow');
			});

			introProjectPage_leftNav_Rerun.onexit(function(css) {
				$('body').removeClass('hide-intro-overflow');
			});
			introProjectPage_leftNav_Rerun.onskip(function(css) {
				$('body').removeClass('hide-intro-overflow');
				resetIntroIntroStep();
			});
			if ( introProjectPage_leftNav_Rerun._options.steps.length ) {
				$('html, body').animate({
					scrollTop: $(".recent-apps-dashboard__content").offset().top - 450
				}, 300);
				$('body').addClass('hide-intro-overflow');
				introProjectPage_leftNav_Rerun.start();
			}
		}

		if ( $('body.bugReport').length ){
			if ( $("#coverage_nav_tab").length < 1 ) {
				if ( !$("#issue_stats_section").hasClass('hidden') ) {
					if (!$('template#manage_issues_intro').length)
						$('body').append(`<template id="manage_issues_intro">
												<!-- Blue -->
												<div class="intro-box">
													<!-- Images section -->
													<div class="intro__head">
														<img class="img-responsive manage_issues_img" style="width:20rem; margin-bottom:-2rem; margin-top:-1.5rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.manage_issues_intro.intro_image}.svg" alt="Issue">
													</div>
													<!-- Title -->
													<div class="intro__body">
														<p class="title">${response.manage_issues_intro.title}</p>
														<p class="descritpion">${response.manage_issues_intro.description}</p>
													</div>
												</div>
											</template>`);
					if (!$('template#issue_counters_intro').length)
						$('body').append(`<template id="issue_counters_intro">
												<!-- Blue -->
												<div class="intro-box">
													<!-- Images section -->
													<div class="intro__head">
														<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.issue_counters_intro.intro_image}.svg" alt="Issue">
													</div>
													<!-- Title -->
													<div class="intro__body">
														<p class="title">${response.issue_counters_intro.title}</p>
														<p class="descritpion">${response.issue_counters_intro.description}</p>
													</div>
												</div>
											</template>`);

					if (!$('template#email_issues_intro').length)
						$('body').append(`<template id="email_issues_intro">
												<!-- Blue -->
												<div class="intro-box">
													<!-- Images section -->
													<div class="intro__head">
														<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.email_issues_intro.intro_image}.svg" alt="Issue">
													</div>
													<!-- Title -->
													<div class="intro__body">
														<p class="title">${response.email_issues_intro.title}</p>
														<p class="descritpion">${response.email_issues_intro.description}</p>
													</div>
												</div>
											</template>`);

					if (!$('template#issues_page_team_member_intro').length )
						$('body').append(`<template id="issues_page_team_member_intro">
											<!-- Blue -->
											<div class="intro-box">
												<!-- Images section -->
												<div class="intro__head">
													<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.issues_page_team_member_intro.intro_image}.svg" alt="Issue">
												</div>
												<!-- Title -->
												<div class="intro__body">
													<p class="title">${response.issues_page_team_member_intro.title}</p>
													<p class="descritpion">${response.issues_page_team_member_intro.description}</p>
												</div>
											</div>
										</template>`);
				}
			}

			if ( !$(".issue-list-sort-filter .js-toggle-filter-opt.hidden-xs").hasClass('hidden') && !$(".issue-list-sort-filter .js-sort-container.hidden-xs").hasClass('hidden') ) {
				if (!$('template#sort_and_filter_issues_intro').length)
						$('body').append(`<template id="sort_and_filter_issues_intro">
											<!-- Blue -->
											<div class="intro-box">
												<!-- Images section -->
												<div class="intro__head">
													<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.sort_and_filter_issues_intro.intro_image}.svg" alt="Issue">
												</div>
												<!-- Title -->
												<div class="intro__body">
													<p class="title">${response.sort_and_filter_issues_intro.title}</p>
													<p class="descritpion">${response.sort_and_filter_issues_intro.description}</p>
												</div>
											</div>
										</template>`);
			}
			if (!$('template#boardview_btn_issues_intro').length)
				$('body').append(`<template id="boardview_btn_issues_intro">
									<!-- Blue -->
									<div class="intro-box">
										<!-- Images section -->
										<div class="intro__head">
											<img class="img-responsive" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.boardview_btn_issues_intro.intro_image}.svg" alt="Board View">
										</div>
										<!-- Title -->
										<div class="intro__body">
											<p class="title">${response.boardview_btn_issues_intro.title}</p>
											<p class="descritpion">${response.boardview_btn_issues_intro.description}</p>
										</div>
									</div>
								</template>`);

			introIssuePage_Rerun = introJs();
			introIssuePage_Rerun.setOptions({
				nextLabel: "Next",
				skipLabel: "Don’t show this again",
				showBullets:false,
				overlayOpacity:1,
				hidePrev:true,
				disableInteraction:true,
				exitOnOverlayClick: false,
				keyboardNavigation:false,
				tooltipClass: 'ap__intro',
				steps:[]
			});

			introIssuePage_Rerun.onchange(function(targetElement) {
				if ( this._introItems[this._currentStep].name != "sprint_coverage_intro" )
				updateIntroStepRerun(this._introItems[this._currentStep].name);

				if ( this._introItems[this._currentStep].name == "boardview_btn_issues_intro" ){
					$('.board-view-btn').addClass('on-intro-show');
				} else {
					$('.board-view-btn').removeClass('on-intro-show');
				}

				if ( this._introItems[this._currentStep].name != "manage_issues_intro" ){
					$('html, body').animate({
						scrollTop: $("#app-issue-table-container").offset().top - 450
					}, 300);
				}

			});

			if ( $("#coverage_nav_tab").length < 1 ) {
				if ( !$("#issue_stats_section").hasClass('hidden') ) {
					if ($('.issue-view-type .active').attr('data-type') == 'LIST'){
						introIssuePage_Rerun.addSteps([{
							name: "manage_issues_intro",
							position: 'top',
							element: $('#bugReport-table .tabulator-row').first()[0],
							intro:$('#manage_issues_intro').html()
						}]);
					}

											introIssuePage_Rerun.addSteps([{
							name: "issue_counters_intro",
							position: 'right-lower-middle',
							element: $('.total-counts').first()[0],
							intro:$('#issue_counters_intro').html()
						}]);
					
					introIssuePage_Rerun.addSteps([{
						name: "email_issues_intro",
						position: 'issue-list-email',
						element: $('.copy_email').first()[0],
						intro:$('#email_issues_intro').html()
					}]);
					if ( $(".issue-list-top-options ul.team-member-list").length ) {
						introIssuePage_Rerun.addSteps([{
							name: "issues_page_team_member_intro",
							position: 'issue-list-team-member',
							element: $('.team-member-list').first()[0],
							intro:$('#issues_page_team_member_intro').html()
						}]);
					}
				}
			}
			if ( !$(".issue-list-sort-filter .js-toggle-filter-opt.hidden-xs").hasClass('hidden') && !$(".issue-list-sort-filter .js-sort-container.hidden-xs").hasClass('hidden') ) {
									introIssuePage_Rerun.addSteps([{
						name: "sort_and_filter_issues_intro",
						position: 'issue-list-sort-filter',
						element: $('.issue-list-sort-filter').first()[0],
						intro:$('#sort_and_filter_issues_intro').html()
					}]);
							}
			if ( !$("#issue_stats_section").hasClass('hidden') ) {
									introIssuePage_Rerun.addSteps([{
						name: "boardview_btn_issues_intro",
						position: 'issue-list-sort-filter',
						element: $('.board-view-btn').first()[0],
						intro:$('#boardview_btn_issues_intro').html()
					}]);
							}

			introIssuePage_Rerun.oncomplete(function() {
				$('body').removeClass('hide-intro-overflow');
				$('.board-view-btn').removeClass('on-intro-show');
			});

			introIssuePage_Rerun.onexit(function(css) {
				$('body').removeClass('hide-intro-overflow');
				$('.board-view-btn').removeClass('on-intro-show');
			});

			introIssuePage_Rerun.onskip(function(css) {
				$('body').removeClass('hide-intro-overflow');
				$('.board-view-btn').removeClass('on-intro-show');
				resetIntroIntroStep();
			});
			if ( introIssuePage_Rerun._options.steps.length ) {
				$('html, body').animate({
					scrollTop: $("#app-issue-table-container").offset().top - 400
				}, 300);
				$('body').addClass('hide-intro-overflow');
				introIssuePage_Rerun.start();
			}
		}
	}
	var introHelp_Rerun = '';
	function runHelpRerunIntro( response ) {

		if (!$('template#leftnav_restart_tour').length)
			$('body').append(`<template id="leftnav_restart_tour">
									<div class="intro-box">
										<div class="intro__head">
											<img class="img-responsive" style="width: 24rem;" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130//img/intro/${response.leftnav_restart_tour_intro.intro_image}.svg" alt="Add Issue">
										</div>
										<div class="intro__body">
											<p class="title">${response.leftnav_restart_tour_intro.title}</p>
											<p class="descritpion">${response.leftnav_restart_tour_intro.description}</p>
										</div>
									</div>
								</template>`);

		introHelp_Rerun = introJs();
		introHelp_Rerun.setOptions({
			doneLabel: "Explore",
			showBullets:false,
			overlayOpacity:1,
			hidePrev:true,
			hideSkip:true,
			disableInteraction:true,
			exitOnOverlayClick: false,
			keyboardNavigation:false,
			tooltipClass: 'ap__intro',
			steps:[]
		});

		introHelp_Rerun.addSteps([{
			name: "leftnav_restart_tour_intro",
			position: "leftnav-restart-tour",
			element: $('.leftnav-tour-restart')[0],
			intro:$('#leftnav_restart_tour').html()
		}]);


		introHelp_Rerun.onchange(function(targetElement) {
			$('.introjs-skipbutton').show();
			updateIntroStepRerun(this._introItems[this._currentStep].name);
		});

		introHelp_Rerun.oncomplete(function() {
			$('body').removeClass('hide-intro-overflow')
		});

		introHelp_Rerun.onexit(function(css) {
			$('body').removeClass('hide-intro-overflow');
		});

		introHelp_Rerun.start();
		$('.introjs-skipbutton').hide();

	}

	function generateClickUpTasksList( appId, teamId ) {
		$.post('https://my.bugasura.io/clickup/generateTasksListFile',{
			appId: appId,
			teamId: teamId,
		},function(response){
			console.log("Generate ClickUp Tasks List Response",response);
		},'json')
	}

	function updateIntroStepRerun( name ) {

		switch( name ) {
			case 'leftnav_projects_intro' :
			case 'leftnav_my_dashboard_intro' :
			case 'leftnav_wizard_intro' :
			case 'leftnav_release_feature_intro' :
			case 'leftnav_settings_intro' :
			case 'leftnav_user_profile_intro' :
			case 'leftnav_restart_tour' :
			case 'leftnav_restart_tour_intro' :
				categoryName = "PLATFORM_LEFTNAV_INTRO";
				break;
			case 'email_issues_intro' :
			case 'manage_issues_intro' :
			case 'sort_and_filter_issues_intro' :
			case 'boardview_btn_issues_intro' :
			case 'issue_counters_intro' :
			case 'issues_page_team_member_intro' :
				categoryName = "PLATFORM_ISSUES_INTRO";
				break;
			case 'manage_team_intro' :
				categoryName = "PLATFORM_TEAM_INTRO";
				break;
			case 'manage_project_intro' :
			case 'create_project_intro' :
				categoryName = "PLATFORM_PROJECT_INTRO";
				break;
		}

		$.post('https://my.bugasura.io/account/updateIntroStep',{
			name: name,
			category: categoryName,
		},function(response){
			if( response.status == "OK") {

				//Mixpanel tracking for completed tour
				if( name == "leftnav_user_profile_intro" ){

					if ( typeof registerMIXPEvent === 'function' )registerMIXPEvent("Completed tour");
				}
				console.log(`The intro step details is updated - ${name}`);
			} else {
				console.log(`Error while updating intro step details - ${name}`);
			}
		},'json');
	}

	function addUpdateReaction( testResultsId, commentId, isLiked, isIssueReaction, thisElem ) {
		var url = 'https://my.bugasura.io/commentReaction/addUpdate';
		if ( isIssueReaction == 1 ) {
			url = 'https://my.bugasura.io/issueReaction/addUpdate';
			commentId = '';
		}
		var mainParentElem = thisElem.parent();
		var likeCount = mainParentElem.find('.js-reaction.like').data('count') ? mainParentElem.find('.js-reaction.like').data('count'): 0;
		var dislikeCount = mainParentElem.find('.js-reaction.dislike').data('count') ? mainParentElem.find('.js-reaction.dislike').data('count'): 0;
		$.post(url,{
			testResultsId: testResultsId,
			commentId: commentId,
			isLiked: isLiked
		},function(response){
			if ( response.status != 'OK' ) {
				toastrMsg(response.message, 'error', true);
				if ( isLiked ) {
					likeCount = likeCount > 0? likeCount-1: 0;
					if ( mainParentElem.find('.js-reaction.dislike').hasClass('prev-active') ) {
						dislikeCount++;
					}
				} else {
					dislikeCount = dislikeCount > 0? dislikeCount-1: 0;
					if ( mainParentElem.find('.js-reaction.like').hasClass('prev-active') ) {
						likeCount++;
					}
				}
				updateReactionCount( testResultsId, commentId, likeCount, dislikeCount )
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).removeClass('active');
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].prev-active`).removeClass('prev-active').addClass('active');
			} else {
				var isPrevLiked = mainParentElem.find('.prev-active.like').length;
				mainParentElem.find('.prev-active').removeClass('prev-active');
				if ( typeof response.reactionDetails != 'undefined' && response.reactionDetails['liked_count'] != 'undefined' ) {
					likeCount = response.reactionDetails['liked_count'];
					dislikeCount = response.reactionDetails['disliked_count'];
					updateReactionCount( testResultsId, commentId, likeCount, dislikeCount );
				}
				if ( isIssueReaction && $('#bugReport-table').length > 0 && $('.bug-filter-types.selected-sort-item .bug-sort-btns[data-column="most_liked"]').length ) {
					if ( typeof loadIssueList == 'function' && ( isPrevLiked || isLiked ) ) {
						var currPageNo = Number($("#currentPageNo").val().trim());
						loadIssueList( currPageNo );
					}
				}
			}
			mainParentElem.removeClass('js-disabled');
		},'json')
	}

	function removeReaction( testResultsId, commentId, isIssueReaction, thisElem ) {
		var url = 'https://my.bugasura.io/commentReaction/delete';
		if ( isIssueReaction == 1 ) {
			url = 'https://my.bugasura.io/issueReaction/delete';
			commentId = '';
		}
		var mainParentElem = thisElem.parent();
		var likeCount = mainParentElem.find('.js-reaction.like').data('count') ? mainParentElem.find('.js-reaction.like').data('count'): 0;
		var dislikeCount = mainParentElem.find('.js-reaction.dislike').data('count') ? mainParentElem.find('.js-reaction.dislike').data('count'): 0;
		$.post(url,{
			testResultsId: testResultsId,
			commentId: commentId
		},function(response){
			if ( response.status != 'OK' ) {
				toastrMsg(response.message, 'error', true);
				var likeCount = mainParentElem.find('.js-reaction.like').data('count') ? mainParentElem.find('.js-reaction.like').data('count'): 0;
				var dislikeCount = mainParentElem.find('.js-reaction.dislike').data('count') ? mainParentElem.find('.js-reaction.dislike').data('count'): 0;
				if ( mainParentElem.find('.js-reaction.like').hasClass('prev-active') ) {
					likeCount++;
				}
				if ( mainParentElem.find('.js-reaction.dislike').hasClass('prev-active') ) {
					dislikeCount++;
				}
				updateReactionCount( testResultsId, commentId, likeCount, dislikeCount );
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).removeClass('active');
				$(`.js-reaction[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].prev-active`).removeClass('prev-active').addClass('active');
			} else {
				var isPrevLiked = mainParentElem.find('.prev-active.like').length;
				mainParentElem.find('.prev-active').removeClass('prev-active');
				if ( typeof response.reactionDetails != 'undefined' && response.reactionDetails['liked_count'] != 'undefined' ) {
					likeCount = response.reactionDetails['liked_count'];
					dislikeCount = response.reactionDetails['disliked_count'];
					updateReactionCount( testResultsId, commentId, likeCount, dislikeCount );
				}
				if ( isIssueReaction && $('#bugReport-table').length > 0 && $('.bug-filter-types.selected-sort-item .bug-sort-btns[data-column="most_liked"]').length ) {
					if ( typeof loadIssueList == 'function' && isPrevLiked ) {
						var currPageNo = Number($("#currentPageNo").val().trim());
						loadIssueList( currPageNo );
					}
				}
			}
			mainParentElem.removeClass('js-disabled');
		},'json')
	}

	function updateReactionCount( testResultsId, commentId, likeCount, dislikeCount ) {
		likeCount = likeCount > 0? likeCount: 0
		dislikeCount = dislikeCount > 0? dislikeCount: 0
		$(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}']`).data('count',likeCount);
		$(`.js-reaction.dislike[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}']`).data('count',dislikeCount);
		$(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'] .count`).text(likeCount).removeClass('hidden');
		$(`.js-reaction.dislike[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'] .count`).text(dislikeCount).removeClass('hidden');
		if ( likeCount == 0 )
			$(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'] .count`).addClass('hidden');
		if ( dislikeCount == 0 )
			$(`.js-reaction.dislike[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'] .count`).addClass('hidden');
		// Update the tooltip
		if ( $(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'][data-original-title]`).length ) {
			$(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).attr('data-original-title','Liked').tooltip('hide');
			$(`.js-reaction.like[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}']:not(.active)`).attr('data-original-title','Like').tooltip('hide');
			$(`.js-reaction.dislike[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}'].active`).attr('data-original-title','Disliked').tooltip('hide');
			$(`.js-reaction.dislike[data-testresults_id='${testResultsId}'][data-comment_id='${commentId}']:not(.active)`).attr('data-original-title','Dislike').tooltip('hide');
		}
	}

	function getReactionsDetails( testResultsId, commentId ) {
		$.post('https://my.bugasura.io/issueCommentReaction/get',{
			testResultsId: testResultsId,
			commentId: commentId
		},function(response){
			if ( response.status != 'OK' ) {
				toastrMsg(response.message, 'error', true);
			} else {
				console.log(response);
			}
		},'json')
	}

</script>

										<div id="footer_content" class="container-fluid footer-container" >
	<div class="row">
	  <div class="col-md-12 footer-content text-center footer-content-center footer-content--new  ">
			  <ul class="list-inline">
				  <li><a href="https://moolya.com" class="text-capitalize" target="_blank">© 2024 Moolya. All Rights Reserved.</a></li>
			  					  <li class="hidden-xs hidden"><a href="http://appachhi.com/privacy-policy/">Privacy policy </a></li>
				  <li class="hidden-xs hidden">|</li>
				  <li class="hidden-xs hidden"><a href="http://appachhi.com/terms-conditions/">Terms & Conditions</a></li>
			  </ul>
		</div>
	</div>
</div>

					</div>
	</body>
	<!-- Chats.js Plugin -->
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/jquery-ui.js"></script>
												<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	<!-- Latest compiled and minified JavaScript -->
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/bootstrap.min.js"></script>
			<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/base.js"></script>
			<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/style.js"></script>
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/jquery-validator/jquery.validate.min.js"></script>
		<script defer type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/bootstrap-tagsinput.js"></script>
		<!--  -->
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/select2.min.js"></script>
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/jquery.multi-select.js"></script>
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/jquery.lazy.min.js"></script>
				<script defer type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/cropper.min.js"></script>
						<script defer type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/zoom.js"></script>
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/Chart.min11.js"></script>
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/bootstrap-editable.min.js"></script>
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/chartjs-plugin-datalabels.min.js"></script>
			<!-- <script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/lobipanel.js"></script> -->
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/material.min.js"></script>
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/wavesurfer/wavesurfer.min.js"></script>
	<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/wavesurfer/wavesurfer.microphone.min.js"></script>
	<!-- <script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/gauge.min.js"></script> -->
	<!-- <script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/html2canvas.min.js"></script> -->
	<!-- documentation: https://github.com/CodeSeven/toastr -->
	<script  type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/toaster/toastr.min.js"></script>
		<script type="text/javascript" src="https://d15iyw5ec6tqi1.cloudfront.net/assets20240326111130/js/plugins/intro.min.js"></script>
				<!-- Analytics -->
		
	
		<!-- Lucky orange OLD -->
		<script type='text/javascript'>

		    var email_lo = "piyushwaghmarehere@gmail.com";
			var email_domain_lo = email_lo.split('@').pop();
			var today = new Date();
			//console.log(email_domain_lo);
			//console.log(today.getDay());

			if (email_domain_lo !== 'cloudnix.com' && email_domain_lo !== 'moolya.com' && today.getDay() !== 0) {

				window.__lo_site_id = 210255;
				(function () {
					var wa = document.createElement('script'); wa.type = 'text/javascript'; wa.async = true;
					wa.src = 'https://d10lpsik1i8c69.cloudfront.net/w.js';
					var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(wa, s);
				})();

								var emailId = "piyushwaghmarehere@gmail.com";
				window._loq = window._loq || [];
				window._loq.push(["tag", emailId]);
				// Below timeinteval set user emaild when user is idle mode 
				setInterval(function () {
					registerEvent(["LO"], emailId, "", "", "");
				}, 10 * 60 * 1000);
				
			}
		</script>

		<!--ClickMeter.com code for on click conversion: Moolya -->
		<script type='text/javascript'>
			var ClickMeter_conversion_id = '2392049085D3446181DADC03D55B8C9C';
			var ClickMeter_conversion_value = '0.00';
			var ClickMeter_conversion_commission = '0.00';
			var ClickMeter_conversion_commission_percentage = '0.00';
			var ClickMeter_conversion_parameter = 'empty';
		</script>
		<script type='text/javascript' id='cmconvscript' src='//s3.amazonaws.com/scripts-clickmeter-com/js/conversionOnClick.js'></script>
	
	<!-- Global site tag (gtag.js) - Google Analytics -->
	<!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-PZS9MRFX2T"></script> OLD-->
	<script async src="https://www.googletagmanager.com/gtag/js?id=UA-191709728-1"></script>
	<script>
		window.dataLayer = window.dataLayer || [];
		function gtag(){dataLayer.push(arguments);}
		gtag('js', new Date());
		gtag('config', 'UA-191709728-1');
	</script>

	<!-- Google Tag Manager -->
	<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
	new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
	j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
	'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
	})(window,document,'script','dataLayer','GTM-K52TFCXZ');</script>
	<!-- End Google Tag Manager -->

	<!-- Google Tag Manager (noscript) -->
	<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K52TFCXZ"
	height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
	<!-- End Google Tag Manager (noscript) -->
	
	

						<!-- Signed Up user -->
			<!-- Freshchat -->
			<script>
				window.fcWidgetMessengerConfig = {
								firstName: "Piyush",
								email: "piyushwaghmarehere@gmail.com",
								meta: {
									cf_user_id: "70292"
								}
				}
			</script>
			<script src='//in.fw-cdn.com/30685332/370541.js' chat='true'></script>
				
	

		<script type="text/javascript">
		//Initialize utm parameter for mixpanel
					var utm_param = {
				"utm_source":"Direct",
				"utm_medium":"Direct",
				"utm_campaign":"Direct"
			};
				/*  
			Function to register and track user actions/events on multiple tracking platforms like Google Analytics, Luckyorange etc.
			Params
				destination - Array(Platfroms like GA,LO etc)
				eventName - Event labels defined by Avinash like 10_LANDED, 20_OPEN_SIGNUP, 30_SIGNEDUP etc.
				eventCategory - Functionality of the event like Signup, Issue, Teams etc.
				eventAction - Brief about the action use has take Ex: 'Landed on bugasura.io', 'Went to Signup page'
		*/
		function registerEvent(destination, eventName, eventCategory, eventAction, eventValue) {
							if ( destination.indexOf("LO") !== -1 ) {
					// Register luckyorange tag event
					window._loq = window._loq || []; 
					window._loq.push(["tag", eventName]);
					// console.log("Registered "+eventName+" Luckyorange Event");
				}
						if ( destination.indexOf("GA") !== -1 ) {
				// Register google analytics event
				registerGAEvent(eventName, eventCategory, eventAction, eventValue);
			}
		}
		function registerGAEvent(eventName, eventCategory, eventAction, eventValue) {
			if (typeof gtag === 'function') {
				gtag('event', eventAction, {
					'event_category': eventCategory,
					'event_label': eventName,
					'value': eventValue,
					'non_interaction': true
				});
				// console.log("Registered "+eventName+" gtag Event");
			} else {
				setTimeout(function(){
					registerGAEvent(eventName, eventCategory, eventAction, eventValue);
				},500);
			}
		}
		//Get cookie value
		function getCookie(cname) {
		  let name = cname + "=";
		  let decodedCookie = decodeURIComponent(document.cookie);
		  let ca = decodedCookie.split(';');
		  for(let i = 0; i < ca.length; i++) {
		    let c = ca[i];
		    while (c.charAt(0) == ' ') {
		      c = c.substring(1);
		    }
		    if (c.indexOf(name) == 0) {
		      return c.substring(name.length, c.length);
		    }
		  }
		  return "";
		}

		//function for mixpanel event tracking
		function registerMIXPEvent(eventName, eventSProperty ={}, eventProperty ={}, identifyUser = 0) {
								if ( identifyUser ) {
						var email = eventSProperty.Email;
						const [name,email_domain] = email.split('@');
						if ( email_domain == 'appachhi.com' || email_domain == 'moolya.com')
							return;
						eventSProperty = Object.assign(eventSProperty,utm_param);
						eventSProperty = Object.assign(eventSProperty,{"Email Domain":email_domain});
					} else {
						var email = "piyushwaghmarehere@gmail.com";
						var user_id = "70292";
						const [name,email_domain] = email.split('@');
						eventSProperty = Object.assign(eventSProperty,utm_param);
						eventSProperty = Object.assign(eventSProperty,{"Email Domain":email_domain});
						eventSProperty = Object.assign(eventSProperty,{"Email":email});
						eventSProperty = Object.assign(eventSProperty,{"Platform user id":user_id});
					}
					
						Property = Object.assign({},eventSProperty,eventProperty);
						var userWebsiteId ="";
						var userWebsiteIdentified = getCookie("mxIdentify");
						if(userWebsiteIdentified == 0)userWebsiteId=getCookie("mxdistinctId");
																		console.log("Request Initiated");
						console.log(Property);
						console.log("EventName",eventName);
						console.log("Website Id",userWebsiteId);
						console.log("hash="+"28bc98b377aeb239a4cdc3a2f9accb5b");
						console.log("timestamp="+"1717149369");

					//Make Api request
					fetch('https://bugasura.io/mp', {
						method: 'POST',
						body: JSON.stringify({
							eventName: eventName,
							eventProperty: Property,
							userWebsiteId: userWebsiteId,
							hash: "28bc98b377aeb239a4cdc3a2f9accb5b",
							timestamp: "1717149369"
						}),
						headers: { 'Content-Type': 'application/json' }
					}).then(result => result.json())
						.then((response) => {
							if (response.status == "SUCCESS") {
								if (response.identify) {
									document.cookie = 'mxIdentify=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
									document.cookie = "mxIdentify=1; path=/; domain=.bugasura.io; SameSite=None; Secure";
									console.log("identified");
								}
								console.log('Response: Success');
							}
							else {
								console.log('Response:Error');
							}
						})
					}
	</script>

		<script type="text/javascript">

		$(document).ready(function (){
							init();
					});

		function init() {
							componentHandler.upgradeAllRegistered();
						$('.get-inpage').unbind().click(get_inpage);						// GET these hrefs in page

			$(".leftnav-toggle").unbind("click").on('click',function () {
				if ($("body").hasClass("minimized")) {
					showLeftnav(this);
				} else {
					hideLeftnav(this);
				}
			});

			$(".leftnav-menu-wrapper").unbind("click").click(function(){
				$(".leftnav-toggle").click();
			});
		}

		function checkEndTransition() {
			var flag = true;
			if ($('.js-overview-link .ap__nudge').length != 0) {
				$('.sidebar-tabs').off('transitionend webkitTransitionEnd oTransitionEnd')
				.on('transitionend webkitTransitionEnd oTransitionEnd',function (e) {
					if (flag == true) {
						$.when($(this)).done(function() {
							console.log(e);
							console.log("Finished");
							var val = $(this);
							$('.nav__overflow--enclosure, .nav-stacked.sidebar-tabs').toggleClass("u-overflow-visible");
							$('.js-overview-link .ap__nudge').toggleClass('animate');
						});
					}
					flag = false;
				});
			}
		}

		function showLeftnav(caller) {
			checkEndTransition();
			if (caller !== undefined) $(caller).removeClass('minimized');
			$("body").removeClass("minimized");
			document.cookie = "minimized=0; expires=Sun, 15 Jan 2023 12:00:00 UTC; path=/";
		}

		function hideLeftnav(caller) {
			checkEndTransition();
			$("body").addClass("minimized");
			if (caller !== undefined) $(caller).addClass('minimized');
			document.cookie = "minimized=1; expires=Sun, 15 Jan 2023 12:00:00 UTC; path=/";
		}
	</script>
</html>
"""