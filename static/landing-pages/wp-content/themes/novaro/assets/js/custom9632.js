// JavaScript Document
jQuery(document).ready(function($){
	"use strict";

	$('.es_subscription_form').addClass('hero-form');
	$('#newsletter-1 form').addClass('newsletter-form'); 
	$('form .es-field-wrap').addClass('input-group');
	$('.es_txt_email').addClass('form-control');
	$('#hero-9 .es_submit_button').addClass('btn btn-green tra-white-hover submit');
	$('#newsletter-1 .es_submit_button').addClass('btn btn-blue blue-hover');

	$(window).on('load', function() {							 
		/*----------------------------------------------------*/
		/*	Preloader
		/*----------------------------------------------------*/
		
		var preloader = $('#loader-wrapper'),
			loader = preloader.find('.cssload-loader');
			loader.fadeOut();
			preloader.delay(400).fadeOut('slow');
				
	});


	$(window).on('scroll', function() {
		/*----------------------------------------------------*/
		/*	Navigtion Menu Scroll
		/*----------------------------------------------------*/	
		
		var b = $(window).scrollTop();
		
		if( b > 72 ){		
			$(".navbar").addClass("scroll");
		} else {
			$(".navbar").removeClass("scroll");
		}				

	});	
			

	/*----------------------------------------------------*/
	/*	Mobile Menu Toggle
	/*----------------------------------------------------*/
	
	$('.navbar-nav li.nav-item.nl-simple, .navbar-collapse span.navbar-text a').on('click', function() {				
		$('#navbarSupportedContent').css("height", "1px").removeClass("in").addClass("collapse");
		$('#navbarSupportedContent').removeClass("show");				
	});


	/*----------------------------------------------------*/
	/*	Animated Scroll To Anchor
	/*----------------------------------------------------*/
	
	$('.header a[href^="#"], .page a.btn[href^="#"], .page a.internal-link[href^="#"]').on('click', function (e) {
		
		e.preventDefault();

		var target = this.hash,
			$target = jQuery(target);
		if( !$target.length  ) 	return;

		if( $('.navbar-collapse').hasClass('show') ){
			$('.navbar-toggler').trigger( 'click' );
		}	
		
		$('html, body').stop().animate({
			'scrollTop': $target.offset().top - 60 // - 200px (nav-height)
		}, 'slow', 'easeInSine', function () {
			window.location.hash = target;
		});
		
	});

	
	/*----------------------------------------------------*/
	/*	ScrollUp
	/*----------------------------------------------------*/
	
	$.scrollUp = function (options) {

		// Defaults
		var defaults = {
			scrollName: 'scrollUp', // Element ID
			topDistance: 600, // Distance from top before showing element (px)
			topSpeed: 800, // Speed back to top (ms)
			animation: 'fade', // Fade, slide, none
			animationInSpeed: 200, // Animation in speed (ms)
			animationOutSpeed: 200, // Animation out speed (ms)
			scrollText: '', // Text for element
			scrollImg: false, // Set true to use image
			activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
		};

		var o = $.extend({}, defaults, options),
			scrollId = '#' + o.scrollName;

		// Create element
		$('<a/>', {
			id: o.scrollName,
			href: '#top',
			title: o.scrollText
		}).appendTo('body');
		
		// If not using an image display text
		if (!o.scrollImg) {
			$(scrollId).text(o.scrollText);
		}

		// Minium CSS to make the magic happen
		$(scrollId).css({'display':'none','position': 'fixed','z-index': '99999'});

		// Active point overlay
		if (o.activeOverlay) {
			$("body").append("<div id='"+ o.scrollName +"-active'></div>");
			$(scrollId+"-active").css({ 'position': 'absolute', 'top': o.topDistance+'px', 'width': '100%', 'border-top': '1px dotted '+o.activeOverlay, 'z-index': '99999' });
		}

		// Scroll function
		$(window).on('scroll', function(){	
			switch (o.animation) {
				case "fade":
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).fadeIn(o.animationInSpeed) : $(scrollId).fadeOut(o.animationOutSpeed) );
					break;
				case "slide":
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).slideDown(o.animationInSpeed) : $(scrollId).slideUp(o.animationOutSpeed) );
					break;
				default:
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).show(0) : $(scrollId).hide(0) );
			}
		});

		// To the top
		$(scrollId).on('click', function(event){
			$('html, body').animate({scrollTop:0}, o.topSpeed);
			event.preventDefault();
		});

	};
	
	$.scrollUp();


	/*----------------------------------------------------*/
	/*	Tabs #1
	/*----------------------------------------------------*/

	$('ul.tabs-1 li').on('click', function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs-1 li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	});


	/*----------------------------------------------------*/
	/*	Single Image Lightbox
	/*----------------------------------------------------*/

	if( $('.image-link').length > 0 ) {
		$('.image-link').magnificPopup({
		  type: 'image'
		});	
	}


	/*----------------------------------------------------*/
	/*	Video Link #1 Lightbox
	/*----------------------------------------------------*/
	
	if( $('.video-popup1').length > 0) {
		$('.video-popup1').each(function(){		
			var videoUrl = $(this).attr( 'href' );
			$(this).magnificPopup({
			    type: 'iframe',			  	  
				iframe: {
					patterns: {
						youtube: {				   
							index: 'youtube.com',
							src: videoUrl					
								}
							}
						}		  		  
			});
		});
	}


	/*----------------------------------------------------*/
	/*	Video Link #2 Lightbox
	/*----------------------------------------------------*/
	
	if( $('.video-popup2').length > 0 ){
		$('.video-popup2').each(function(){		
			var videoUrl = $(this).attr( 'href' );
			$(this).magnificPopup({
			    type: 'iframe',			  	  
				iframe: {
					patterns: {
						youtube: {				   
							index: 'youtube.com',
							src: videoUrl					
								}
							}
						}		  		  
			});
		});
	}


	/*----------------------------------------------------*/
	/*	Video Link #3 Lightbox
	/*----------------------------------------------------*/
	
	if( $('.video-popup3').length > 0 ) {
		$('.video-popup3').each(function(){		
			var videoUrl = $(this).attr( 'href' );
			$(this).magnificPopup({
			    type: 'iframe',			  	  
				iframe: {
					patterns: {
						youtube: {				   
							index: 'youtube.com',
							src: videoUrl					
								}
							}
						}		  		  
			});
		});
	}

	/*----------------------------------------------------*/
	/*	Sticky Bottom Quick
	/*----------------------------------------------------*/

	if( $('.help-btn').length > 0 ) {
		$('.help-btn').on('click', function(){
        $(".sticky-form").toggleClass("open");
        $(this).toggleClass("clicked");
    });
	}

	/*----------------------------------------------------*/
	/*	Testimonials Rotator
	/*----------------------------------------------------*/

	if( $('.icons-carousel').length > 0 ) {
		var owl = $('.icons-carousel');
			if ($('body').hasClass('rtl')) {
				var rtl = true;
			}else{
				var rtl = false;
			}	
			owl.owlCarousel({
				items: 3,
				loop:true,
				autoplay:true,
				navBy: 1,
				dots: false,
				rtl: rtl,
				autoplayTimeout: 2500,
				autoplayHoverPause: true,
				smartSpeed: 900,
				responsive:{
					0:{
						items:1
					},
					767:{
						items:1
					},
					768:{
						items:1
					},
					991:{
						items:1
					},
					1000:{
						items:1
					}
				}
		});
	}




	/*----------------------------------------------------*/
	/*	Screens Carousel Slick
	/*----------------------------------------------------*/
	
	if( $('.screens-carousel').length > 0 ) {
		$('.screens-carousel').slick({
			infinite: true,
			autoplay: true,
			centerMode: true,
			dots: true,
			autoplaySpeed: 3500,
			speed: 1000,
			slidesToShow: 5,
			slidesToScroll: 1,
			variableWidth: true,
			responsive: [
			    {
			      breakpoint: 769,
			      settings: {
			        slidesToShow: 3
			      }
			    },
			    {
			      breakpoint: 480,
			      settings: {
				    dots: false,
			        slidesToShow: 1,
			        variableWidth: false,
			        fade: true,
					cssEase: 'linear'
			      }
			    }
			]
		});
	}	


	/*----------------------------------------------------*/
	/*	Statistic Counter
	/*----------------------------------------------------*/

	if( $('.count-element').length > 0 ){
		$('.count-element').each(function () {
			$(this).appear(function() {
				$(this).prop('Counter',0).animate({
					Counter: $(this).text()
				}, {
					duration: 4000,
					easing: 'swing',
					step: function (now) {
						$(this).text(Math.ceil(now));
					}
				});
			},{accX: 0, accY: 0});
		});
	}


	/*----------------------------------------------------*/
	/*	Testimonials Rotator
	/*----------------------------------------------------*/

	if( $('.reviews-holder').length > 0 ) {
		var owl = $('.reviews-holder');
			owl.owlCarousel({
				items: 3,
				loop:true,
				autoplay:true,
				navBy: 1,
				autoplayTimeout: 4500,
				autoplayHoverPause: true,
				smartSpeed: 1500,
				responsive:{
					0:{
						items:1
					},
					767:{
						items:1
					},
					768:{
						items:2
					},
					991:{
						items:3
					},
					1000:{
						items:3
					}
				}
		});
	}


	/*----------------------------------------------------*/
	/*	Brands Logo Rotator
	/*----------------------------------------------------*/

	if( $('.brands-carousel').length > 0 ){
		var owl = $('.brands-carousel');
			owl.owlCarousel({
				items: 5,
				loop:true,
				autoplay:true,
				navBy: 1,
				nav:false,
				autoplayTimeout: 4000,
				autoplayHoverPause: false,
				smartSpeed: 2000,
				responsive:{
					0:{
						items:2
					},
					550:{
						items:3
					},
					767:{
						items:3
					},
					768:{
						items:4
					},
					991:{
						items:4
					},				
					1000:{
						items:5
					}
				}
		});
	}

	/*----------------------------------------------------*/
	/*	Masonry Grid
	/*----------------------------------------------------*/

	if( $('.grid-loaded').length > 0 ){
		$('.grid-loaded').imagesLoaded(function () {

	        // filter items on button click
	        $('.masonry-filter').on('click', 'button', function () {
	            var filterValue = $(this).attr('data-filter');
	            $grid.isotope({
	              filter: filterValue
	            });
	        });

	        // change is-checked class on buttons
	        $('.masonry-filter button').on('click', function () {
	            $('.masonry-filter button').removeClass('is-checked');
	            $(this).addClass('is-checked');
	            var selector = $(this).attr('data-filter');
	            $grid.isotope({
	              filter: selector
	            });
	            return false;
	        });        
	        
	    });
	}

    /*----------------------------------------------------*/
	/*	Blog Grid
	/*----------------------------------------------------*/
	if( $('.grid-loaded').length > 0 ){
		$('.grid-loaded').imagesLoaded(function () {
	        var $grid = $('.masonry-wrap').isotope({
	            itemSelector: '.masonry-item',
	            percentPosition: true,
	            transitionDuration: '0.7s',
	            masonry: {
	              columnWidth: '.masonry-item',
	            }
	        });	        
	    });
    }   

	$.ajaxChimp.translations.cm = {
		'submit': 'Submitting...',
		0: 'We have sent you a confirmation email',
		1: 'Please enter your email address',
		2: 'An email address must contain a single @',
		3: 'The domain portion of the email address is invalid (the portion after the @: )',
		4: 'The username portion of the email address is invalid (the portion before the @: )',
		5: 'This email address looks fake or invalid. Please enter a real email address'
	};

	if( NOVARO.animation){
	    var NovaroAnimation = new WOW({
	      boxClass:     'wow',      // default
	      animateClass: 'animated',
	      mobile: false
	    });
	    NovaroAnimation.init();
	}


	function novaro_megamenu(){  
    	var width, pos, left;
	    $('.novaro-megamenu-nav-item').each(function(){
	    	var target = $(this).data('target_class');
	      	var container = $(this).closest(target);
	      	width = container.innerWidth();
	      	if( target == 'custom_width' ){
	      		var custom_width = parseInt($(this).data('custom_width'));
	      		if(custom_width > 0){
	      			width = custom_width;
	      			$(this).closest('.dropdown-menu').css({minWidth: width, maxWidth: width });
	      			$(this).closest('.dropdown-menu').addClass('novaro-megamenu-has-custom-width');
	      		}
	      	}else{
	      		pos = $(this).offset();
	      		left = pos.left - (container.offset()).left;
	      		$(this).closest('.dropdown-menu').css({left : - left, minWidth: width, maxWidth: width });
	      	}
	      	
	      	
	    })

	}	  

	$(window).on( 'resize', function(){
		if ( $(window).width() > 991 ) {
		  novaro_megamenu();
		}else{
		  $('.novaro-megamenu-nav-item').closest('.dropdown-menu').css({});
		}
	})

	novaro_megamenu();

	var preloader = $('#loader-wrapper'),
	loader = preloader.find('.loading-center');
	loader.fadeOut();
	preloader.delay(1500).fadeOut('slow');

	new WOW().init();


    $('table').addClass('table');
	$('blockquote').addClass('blockquote');
	$('.single-widget select, .footer-widget select, .orderby').addClass('custom-select');

	/*----------------------------------------------------*/
	/*	Email Subscribers form
	/*----------------------------------------------------*/

	$('.es-name input[type="text"]').addClass('form-control');
	$('.es-email input[type="email"]').addClass('form-control');
	$('.hero-section .es-email').addClass('d-grid d-md-flex');
	$('.newsletter-1 .newsletter-form .es-email').addClass('d-grid d-md-flex');
	$('.es-submit input[type="submit"]').addClass('btn btn-primary');
	$('.gjs-row').addClass('gjs-row-custom').removeClass('gjs-row');

	$('div.gjs-cell').each(function() {
		var $cell = $(this);
		if($.trim($cell.html())==='') {
		   $cell.parent().remove();
		}
   });

	$('.footer .newsletter-widget .es-email .btn').attr('type', 'hidden');
	$('<button type="submit" name="submit"><i class="far fa-arrow-alt-circle-right"></i></button>').insertAfter('.footer .newsletter-widget .es-email .btn');

    // Woocommerce scripts
	/* count control */
    $(document).on('click', '.count-control', function(){
    	var $quantity_input = $(this).closest('.quantity').find('.qty');
        var old = parseInt($quantity_input.val());
        var step = parseInt($quantity_input.attr('step'));
        if($(this).hasClass('plus')){
          $quantity_input.val(old+step);          

        }else{
          if(old > 1){
            $quantity_input.val(old-step);
          }     
        }

        $(this).closest('form').find('button[type="submit"]').prop('disabled', false);
        return false;
    });   


});
