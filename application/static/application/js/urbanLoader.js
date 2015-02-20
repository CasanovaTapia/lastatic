$( '#urban' ).click( function( e ) {
  e.preventDefault();
  $.swipebox( [
    { src:'{{STATIC_URL}}application/img/urban/pic1.jpg'},
    { src:'{{STATIC_URL}}application/img/urban/pic2.jpg'}
  ] );
} );
