(function(){
  var btn=document.querySelector('.menu-btn'), nav=document.getElementById('hauptmenue');
  function close(){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.querySelector('.sr-only').textContent='Menü öffnen';}
  if(btn&&nav){
    btn.addEventListener('click',function(){
      var open=nav.classList.toggle('open');
      btn.setAttribute('aria-expanded',open);
      btn.querySelector('.sr-only').textContent=open?'Menü schließen':'Menü öffnen';
    });
    nav.addEventListener('click',function(e){ if(e.target.tagName==='A') close(); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&nav.classList.contains('open')){close();btn.focus();} });
  }

  var y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();

  var form=document.getElementById('quote-form'), msg=document.getElementById('form-msg');
  if(!form) return;
  var pre=new URLSearchParams(location.search).get('art'), sel=document.getElementById('f-art');
  if(pre&&sel){[].forEach.call(sel.options,function(o){if(o.text===pre)sel.value=o.value;});}
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var bad=[].slice.call(form.querySelectorAll('[required]')).filter(function(el){return !el.checkValidity();});
    if(bad.length){ msg.textContent='Bitte füllen Sie Name, E-Mail, Beschreibung und die Einwilligung aus.'; bad[0].focus(); return; }
    var v=function(id){var el=document.getElementById(id);return el?el.value.trim():'';};
    var body=[
      'Name: '+v('f-name'),
      'Firma: '+v('f-firma'),
      'E-Mail: '+v('f-mail'),
      'Telefon: '+v('f-tel'),
      '',
      'Schildart: '+v('f-art'),
      'Material: '+v('f-mat'),
      'Befestigung: '+v('f-bef'),
      'Stückzahl: '+v('f-menge'),
      'Maße (mm): '+v('f-mass'),
      'Lieferland: '+v('f-land'),
      '',
      v('f-text')
    ].filter(function(l){return !/: $/.test(l);}).join('\n');
    var subject='Angebotsanfrage: '+v('f-art')+(v('f-firma')?' – '+v('f-firma'):'');
    window.location.href='mailto:info@metallschilder24.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
    msg.textContent='Ihr E-Mail-Programm wurde geöffnet. Falls nicht, schreiben Sie uns direkt an info@metallschilder24.com.';
  });
})();
