hiddenNavBar = {
  $menu: $('#menu'),
  init: function () {
    this.resize();
    $('<div id="on-hidden-menu"><div class="toggle "><span></span></div><ul></ul></div>').hide().insertAfter(this.$menu);
    // toggle
    $('#on-hidden-menu .toggle').click(function () {
      $('#on-hidden-menu').toggleClass('open');
    });

    // win load & resize
    $(window).on('load resize', function () {
      hiddenNavBar.resize();
    });
  },
  resize: function () {
    setTimeout(function () {
      var menuWidth = $('ul', this.$menu).width() + 60;
      var winW = $(window).width();

      console.log(menuWidth, winW);

      if (menuWidth > winW) {
        console.log('init');

        $('#on-hidden-menu').show();
        $clone = $('li:not(".on-hidden"):last', this.$menu).addClass('on-hidden').clone();

        if ($clone.parent().size() == 0) {
          $clone.prependTo($('#on-hidden-menu ul'));
        }

        hiddenNavBar.resize();

      } else if (menuWidth + $('li.on-hidden:first').width() < winW) {
        $('li.on-hidden:first').removeClass('on-hidden');
        $('#on-hidden-menu ul li:first').remove();
      }

      if ($('.on-hidden').size() == 0) {
        $('#on-hidden-menu').removeClass('open').hide();
      }
    }, 10);
  }
};

$(function () {
  hiddenNavBar.init();
}) 