<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 6.4.7.2 (Linux)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="2021-06-27T17:02:59.273034635"/>
	<style type="text/css">
		@page { size: 21cm 29.7cm; margin-left: 2cm; margin-right: 1cm; margin-top: 1cm; margin-bottom: 1cm }
		p { margin-bottom: 0.25cm; line-height: 115%; background: transparent }
		h1 { margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h1.western { font-family: "Liberation Serif", serif; font-size: 24pt; font-weight: bold }
		h1.cjk { font-family: "Noto Serif CJK SC"; font-size: 24pt; font-weight: bold }
		h1.ctl { font-family: "Lohit Devanagari"; font-size: 24pt; font-weight: bold }
		h2 { margin-top: 0.35cm; margin-bottom: 0.21cm; background: transparent; page-break-after: avoid }
		h2.western { font-family: "Liberation Serif", serif; font-size: 18pt; font-weight: bold }
		h2.cjk { font-family: "Noto Serif CJK SC"; font-size: 18pt; font-weight: bold }
		h2.ctl { font-family: "Lohit Devanagari"; font-size: 18pt; font-weight: bold }
		a:link { color: #000080; so-language: zxx; text-decoration: underline }
		a:visited { color: #800000; so-language: zxx; text-decoration: underline }
	</style>
</head>
<body lang="de-DE" link="#000080" vlink="#800000" dir="ltr"><h1 class="western">
Automatischer Tischkicker</h1>
<h2 class="western">Beschreibung</h2>
<p>Ein umgebauter Tischkicker welcher in der Lage ist Tore
automatisch zu zählen und Spielstände von bis zu 16 Spielern zu
Speichern. 
</p>
<h2 class="western">Funktionsweise</h2>
<p>Der umgebaute Tischkicker verfügt über 2 Terminals mit jeweils
einem 2x16LCD-Display und 5 Schaltern. 4 der 5 Schalter dienen zur
Eingabe der Spieler-ID (ein max. vierstelliger Binärwert (0=0000,
1=0001 usw.)(daher 16 Spieler)), der verbleibende Schalter dient zum
bestätigen der ID.  Des weiten verfügt der Tischkicker über 2 rote
Buttons welche auf der jeweiligen Seite ein Tor (Punkt) abziehen.</p>
<p>Tore werden mit Hilfe von Lichtschranken an der Ballführung
zwischen Tor und Ballausgabe gezählt.</p>
<p>Zur Ansteuerung der Komponenten wird ein Raspberry Pi pico
verwendet.</p>
</body>
</html>
