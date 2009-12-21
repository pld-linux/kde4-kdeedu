
%define		_state		unstable
%define		orgname		kdeedu
%define		snap		svn1040395

Summary:	K Desktop Environment - edutainment
Summary(pl.UTF-8):	K Desktop Environment - edukacja i rozrywka
Name:		kde4-kdeedu
Version:	4.3.85
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	855f81b8a597803da8f88574d36bd328
Patch0:		%{name}-findindi.patch
BuildRequires:	Qt3Support-devel
BuildRequires:	QtDesigner-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScriptTools-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	automoc4
BuildRequires:	boost-python-devel
BuildRequires:	cfitsio-devel
BuildRequires:	eigen-devel >= 2.0.51
BuildRequires:	gmm-devel
BuildRequires:	gpsd-devel
BuildRequires:	gsl-devel >= 1.8
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libindi-devel
BuildRequires:	libnova-devel
BuildRequires:	libqalculate-devel >= 0.9.5
BuildRequires:	libxslt-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-facile
BuildRequires:	openbabel-devel >= 2.2.0
BuildRequires:	pkgconfig
#BuildRequires:	python-PyKDE4
BuildRequires:	python-sip-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xplanet >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - edutainment.

%description -l pl.UTF-8
K Desktop Environment - edukacja i rozrywka.

%package devel
Summary:	Header files for kdeedu libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek kdeedu
Group:		X11/Development/Libraries
Requires:	%{name}-libkdeeducore = %{version}-%{release}
Requires:	%{name}-marble = %{version}-%{release}

%description devel
Header files for kdeedu libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek kdeedu.

%package blinken
Summary:	KDE version of the well-known game Simon Says
Summary(pl.UTF-8):	Wersja KDE dobrze znanej gry "Simon Says"
Group:		X11/Applications/Science

%description blinken
KDE version of the well-known game Simon Says.

%description blinken -l pl.UTF-8
Wersja KDE dobrze znanej gry "Simon Says".

%package cantor
Summary:	Cantor
Summary(pl.UTF-8):	Cantor
Group:		X11/Applications/Science

%description cantor
Cantor.

%description cantor -l pl.UTF-8
Cantor.

%package rocs
Summary:	Rocs Graph Theory
Summary(pl.UTF-8):	Rocs - Teoria Wykresów
Group:		X11/Applications/Science

%description rocs
Graph Theory Tool for Professors and Students.

%description rocs -l pl.UTF-8
Teoria wykresów dla profesorów oraz studentów.

%package kalzium
Summary:	A Periodic System of Elements database
Summary(pl.UTF-8):	Baza danych Układu Okresowego Pierwiastków
Group:		X11/Applications/Science

%description kalzium
A Periodic System of Elements database. Kalzium provides you with all
kind of information about the PSE (Periodic System of Elements.) You
can lookup lots of information about the elements and also use
visualizations to show them.

%description kalzium -l pl.UTF-8
Baza danych Układu Okresowego Pierwiastków. Kalzium dostarcza
wszelkie informacje dotyczące UOP, informacje o pierwiastkach oraz
ich wizualizacje.

%package kanagram
Summary:	Guess anagram game
Summary(pl.UTF-8):	Gra w zgadywanie anagramów
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description kanagram
Guess anagram game.

%description kanagram -l pl.UTF-8
Gra w zgadywanie anagramów.

%package kbruch
Summary:	Task generator for calculations with fractions
Summary(pl.UTF-8):	Generator zadań z obliczeniami na ułamkach
Group:		X11/Applications

%description kbruch
KBruch is a small program to generate tasks with fractions. The user
has to solve the given task by entering the right value for numerator
and denominator. The program checks the input and gives feedback. The
task generation can be adjusted by using different parameters. The
user can decide if he wants to solve tasks with addition/subtraction
and/or multiplication/division.

%description kbruch -l pl.UTF-8
Generator zadań z obliczeniami na ułamkach. KBruch to mały program
do generowania zadań z ułamkami. Użytkownik ma rozwiązać zadanie
poprzez wpisanie poprawnej wartości dla licznika i mianownika.
Następnie program sprawdza poprawność danych. Generowanie zadań
można dostosowywać przy pomocy różnych parametrów. Użytkownik
może decydować, czy chce rozwiązywać zadania z
dodawaniem/odejmowaniem i/lub mnożeniem/dzieleniem.

%package kgeography
Summary:	A geography learning program
Summary(pl.UTF-8):	Program do nauki geografii
Group:		X11/Applications/Science

%description kgeography
A geography learning program.

%description kgeography -l pl.UTF-8
Program do nauki geografii.

%package khangman
Summary:	A hangman game
Summary(pl.UTF-8):	Gra w wisielca
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description khangman
KHangMan is a game based on the well known hangman game. A word is
picked in random, the letters are hidden, you must guess the word by
trying a letter after another. Each time you guess a wrong letter, a
picture of a hangman is drawn. You must guess the word before getting
hanged! It is aimed for children aged 6+.

%description khangman -l pl.UTF-8
KHangMan jest grą opartą na popularnej grze w wisielca. Wybierane
jest losowe słowo, którego litery są ukryte. Trzeba zgadnąć to
słowo podając kolejno litery. Za każdym razem, gdy podana litera
nie występuje w słowie, rysowany jest obrazek wisielca. Trzeba
odgadnąć słowo przed powieszeniem! Gra jest przeznaczona dla dzieci
w wieku 6 lat lub więcej.

%package kig
Summary:	Interactive Geometry
Summary(pl.UTF-8):	Interaktywna geometria
Group:		X11/Applications/Science

%description kig
Kig is an application for Interactive Geometry. It's intended to serve
two purposes:
- allow students to interactively explore mathematical figures and
  concepts using the computer.
- serve as a WYSIWYG tool for drawing mathematical figures and
  including them in other documents.

%description kig -l pl.UTF-8
Kig to aplikacja do interaktywnej geometrii. Ma służyć dwóm celom:
- umożliwić uczniom interaktywnie przeglądanie figur i pojęć
  matematycznych przy użyciu komputera
- służyć jako narzędzie WYSIWYG do rysowania figur matematycznych
  i włączania ich do innych dokumentów.

%package kiten
Summary:	A Japanese reference tool
Summary(pl.UTF-8):	Słownik angielsko-japoński
Group:		X11/Applications/Science

%description kiten
Kiten is an application with multiple functions. Firstly, it is a
convenient English to Japanese and Japanese to English dictionary;
secondly, it is a Kanji dictionary, with multiple ways to look up
specific characters; thirdly, it is a tool to help you learn Kanji.

%description kiten -l pl.UTF-8
Kiten to aplikacja o wielu funkcjach. Po pierwsze, jest wygodnym
słownikiem angielsko-japońskim i japońsko-angielskim; po drugie,
jest słownikiem Kanji z wieloma sposobami wyszukiwania określonych
znaków; po trzecie, jest narzędziem pomagającym w nauce Kanji.

%package klettres
Summary:	Helps child to learn alphabet and to read some syllables
Summary(pl.UTF-8):	Pomoc w nauce alfabetu i sylab dla dzieci
Group:		X11/Applications/Science

%description klettres
KLettres is a very simple application that helps a child or an adult
to learn the alphabet and some simple sounds in his own language or in
another language. The program picks up a letter or a syllable in
random, this letter/syllable is displayed and the sound is played. The
user should then type this letter or syllable. Training is done in the
levels where the letter/syllable is not displayed, only the sound is
played. The user does not need to know how to use the mouse, the
keyboard only is needed.

There are five languages available at the moment: Czech, Danish,
Dutch, French and Slovak.

%description klettres -l pl.UTF-8
KLettres to bardzo prosta aplikacja pomagająca dzieciom i dorosłym w
nauce alfabetu i głosek we własnym lub obcym języku. Program losuje
literę lub sylabę, a następnie wyświetla ją i odgrywa dźwięk.
Użytkownik powinien następnie wpisać tę literę lub sylabę. Do
ćwiczeń służą poziomy, gdzie litera/sylaba nie jest wyświetlana,
jedynie dźwięk jest odgrywany. Użytkownik nie musi wiedzieć, jak
używać myszy, wymagana jest tylko klawiatura.

Aktualnie dostępne jest pięć języków: czeski, duński,
holenderski, francuski i słowacki.

%package kmplot
Summary:	Mathematical function plotter
Summary(pl.UTF-8):	Rysowanie wykresów funkcji matematycznych
Group:		X11/Applications/Science

%description kmplot
KmPlot is a mathematical function plotter for the KDE Desktop. It has
a powerful built-in parser. You can plot different functions
simultaneously and combine them to build new functions.

%description kmplot -l pl.UTF-8
KmPlot to narzędzie do rysowania wykresów funkcji matematycznych dla
środowiska KDE. Ma wbudowany potężny parser. Można rysować
różne funkcje jednocześnie i łączyć je, aby stworzyć nowe
funkcje.

%package kpercentage
Summary:	A percentage tutor
Summary(pl.UTF-8):	Program do nauki procentów
Group:		X11/Applications/Science

%description kpercentage
A percentage tutor.

%description kpercentage -l pl.UTF-8
Program do nauki procentów.

%package kstars
Summary:	Desktop planetarium
Summary(pl.UTF-8):	Planetarium
Group:		X11/Applications/Science
Requires:	kde4-kdeedu-libkdeeducore = %{version}-%{release}

%description kstars
KStars lets you explore the night sky from the comfort of your
computer chair. It provides an accurate graphical representation of
the night sky for any date, from any location on Earth. The display
includes 126,000 stars to 9th magnitude (well below the naked-eye
limit), 13,000 deep-sky objects (Messier, NGC and IC catalogs), all
planets, the Sun and Moon, hundreds of comets and asteroids, the Milky
Way, 88 constellations, and guide lines such as the celestial equator,
the horizon and the ecliptic.

%description kstars -l pl.UTF-8
KStars pozwala przeglądać nocne niebo z wygodą krzesła przy
komputerze. Dostarcza dokładną graficzną reprezentację nocnego
nieba dla dowolnej daty, z dowolnego miejsca na Ziemi. Obraz zawiera
126000 gwiazd do 9. wielkości (znacznie poza zasięgiem
nieuzbrojonego oka), 13000 obiektów (katalogi Messiera, NGC i IC),
wszystkie planety, Słońce i Księżyc, setki komet i asteroid,
Drogę Mleczną, 88 konstelacji oraz linie prowadzące takie jak
równik astronomiczny, horyzont i ekliptykę.

%package ktouch
Summary:	Program for learning touch typing
Summary(pl.UTF-8):	Program do nauki maszynopisania
Group:		X11/Applications/Science

%description ktouch
KTouch is a program for learning to touch type. It provides you with
text to train on, and adjust to different levels, depending on how
good you are. It can display which key to press next, and the correct
finger to use. It's the perfect touch typing tutor, you learn typing
with all the fingers without looking at the keys, in an step by step
way. It is convenient for all ages, and the perfect typing tutor for
schools, universities and individuals.

%description ktouch -l pl.UTF-8
KTouch to program do nauki maszynopisania. Dostarcza tekst do
ćwiczeń, dostosowany do różnych poziomów, zależnie od stopnia
zaawansowania. Może wyświetlać, który klawisz trzeba nacisnąć, i
którego palca należy użyć. Jest świetnym programem do nauki
maszynopisania, uczy pisać wszystkimi palcami bez patrzenia na
klawisze, krok po kroku. Jest wygodny w każdym wieku, jest świetny
dla szkół, uniwersytetów i jednostek.

%package kturtle
Summary:	A Logo interpreter for KDE
Summary(pl.UTF-8):	Interpreter języka Logo dla KDE
Group:		X11/Applications/Science

%description kturtle
KTurtle is a Logo programming language interpreter for KDE. The Logo
programming language is very easy and thus it can be used by young
children. A unique quality of Logo is that the commands or
instructions can be translated (please see the translation how to if
you want to help in your own language), so the 'programmer' can
program in his or her native language. This makes Logo ideal for
teaching kids the basics of programming, mathematics and geometry. One
of the reasons many children like Logo is because of the turtle, a
programmable icon which can be moved around the screen with simple
commands and can be programmed to draw objects.

KTurtle features:
- integrated Logo interpreter, no need to download any other program
- powerful editor for the Logo commands with syntax highlighting, line
  numbering and more
- nice "playground" for the turtle where your commands visualized
- translation of the Logo commands (among others in: Dutch, French
  German, Latin and Swedish)
- context help for each Logo command

%description kturtle -l pl.UTF-8
KTurtle to interpreter języka programowania Logo dla KDE. Język Logo
jest bardzo łatwy, przez co może być używany przez małe dzieci.
Unikalna jakość Logo polega na tym, że polecenia czy instrukcje
mogą być tłumaczone (proszę zobaczyć howto dla tłumaczy, aby
pomóc przy tłumaczeniu na własny język), dzięki czemu
"programista" może programować w języku ojczystym. To czyni Logo
idealnym do nauki dzieci podstaw programowania, matematyki i
geometrii. Jednym z powodów, dla których wiele dzieci lubi Logo,
jest żółw - programowalna ikona, którą można przesuwać po
ekranie prostymi poleceniami i programować do rysowania obiektów.

Możliwości KTurtle:
- zintegrowany interpreter Logo, nie trzeba ściągać żadnego innego
  programu
- potężny edytor do poleceń Logo z podświetlaniem składni,
  numerowaniem linii itp.
- ładne "boisko" dla żółwia, gdzie wizualizowane są polecenia
- tłumaczenia poleceń Logo (m.in. na język francuski, holenderski,
  łaciński, niemiecki i szwedzki)
- pomoc kontekstowa dla każdego polecenia Logo.

%package kwordquiz
Summary:	A flashcard and vocabulary learning program
Summary(pl.UTF-8):	Program do ćwiczenia słownictwa za pomocą pokazywania kart
Group:		X11/Applications/Science

%description kwordquiz
KWordQuiz is the KDE version of the flashcard and vocabulary learning
program WordQuiz. It is a tool for learning the vocabulary of a new
language. Now you can start to use its power for easy vocabulary
learning.

You build vocabularies in a two-column table (or load them from
kvoctrain's .kvtml). In one column you enter the words or expressions
in one language, and in the other column the corresponding word or
expression in another language. You can also use it to practice other
things, as long as there is a pair-wise relation. Examples are medical
or legal terminology. If you look at the screenshots there is an
example with the different US states and their capitals.

KWordQuiz also features Flashcard, Multiple Choice and Question &
Answer functions. Question & Answer also has a special
Fill-in-the-blank mode.

%description kwordquiz -l pl.UTF-8
KWordQuiz to wersja KDE programu WordQuiz służącego do nauki
słownictwa za pomocą pokazywania kart. Jest to narzędzie do nauki
słownictwa nowego języka. Można zacząć używać jego potencjału
do łatwego uczenia się słownictwa.

Słowniki buduje się w dwukolumnowej tabeli (lub wczytuje z plików
.kvtml z kvoctraina). W jednej kolumnie wpisuje się słowa lub
wyrażenia w jednym języku, a w drugiej kolumnie ich odpowiedniki w
innym języku. Można także używać programu do ćwiczenia innych
rzeczy, jeśli tylko mają parowalną relację - na przykład
terminologii medycznej czy prawniczej. Na screenshotach widać
przykład z różnymi stanami USA i ich stolicami.

KWordQuiz zawiera także funkcje Flashcard (pokazywania kart), testu
wielokrotnego wyboru oraz pytań i odpowiedzi. Pytania i odpowiedzi
mają także specjalny tryb wypełniania luk.

%package libkdeeducore
Summary:	KDE educational module core library
Summary(pl.UTF-8):	Podstawowa biblioteka modułu edukacyjnego KDE
Group:		X11/Libraries

%description libkdeeducore
The core library for education applications in KDE.

%description libkdeeducore -l pl.UTF-8
Podstawowa biblioteka z funkcjami wykorzystywanymi przez aplikacje
edukacyjne w KDE.

%package kalgebra
Summary:	Mathematical calculator for KDE
Summary(pl.UTF-8):	Kalkulator matematyczny dla KDE
Group:		X11/Libraries

%description kalgebra
KAlgebra is a mathematical calculator based on MathML content markup
language.

%description kalgebra -l pl.UTF-8
KAlgebra to kalkulator matematyczny oparty na języku znaczników
MathML.

%package marble
Summary:	Geographical map for KDE
Summary(pl.UTF-8):	Mapa geograficzna dla KDE
Group:		X11/Libraries

%description marble
Marble is a geographical map for KDE.

%description marble -l pl.UTF-8
Marble to mapa geograficzna dla KDE.

%package parley
Summary:	Parley - KDE program to help you memorize things
Summary(pl.UTF-8):	Parley - program dla KDE pomagający w zapamiętywaniu
Group:		X11/Libraries

%description parley
Parley is a KDE program to help you memorize things

%description parley -l pl.UTF-8
Parley to program dla KDE pomagający w zapamiętywaniu

%package step
Summary:	Step: Interactive Physical Simulator
Summary(pl.UTF-8):	Step - interaktywny symulator fizyczny
Group:		X11/Applications
URL:		http://edu.kde.org/step/

%description step
Step is an interactive physical simulator.

It works like this: you place some bodies on the scene, add some
forces such as gravity or springs, then click "Simulate" and Step
shows you how your scene will evolve according to the laws of physics.

You can change every property of bodies/forces in your experiment
(even during simulation) and see how this will change evolution of the
experiment. With Step you can not only learn but feel how physics
works!

%description step -l pl.UTF-8
Step to interaktywny symulator fizyczny.

Działa w ten sposób: umieszcza się na scenie jakieś ciała, dodaje
siły takie jak grawitacja czy sprężyny, a następnie wciska
przycisk "Symuluj" - a Step pokazuje, jak scena będzie się
zmieniała zgodnie z prawami fizyki.

W ramach eksperymentu można zmieniać każdą właściwość
ciał/sił (nawet podczas symulacji) i obserwować, jak zmieni to jego
przebieg. Przy użyciu Stepa można nie tylko nauczyć się, ale i
poczuć, jak działa fizyka.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DEXPERIMENTAL_PYTHON_BINDINGS=FALSE \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang blinken	--with-kde
%find_lang cantor	--with-kde
%find_lang kalgebra	--with-kde
%find_lang kalzium	--with-kde
%find_lang kanagram	--with-kde
%find_lang kbruch	--with-kde
%find_lang kgeography	--with-kde
%find_lang khangman	--with-kde
%find_lang kig		--with-kde
%find_lang kiten	--with-kde
%find_lang klettres	--with-kde
%find_lang kmplot	--with-kde
#%find_lang kpercentage	--with-kde
%find_lang kstars	--with-kde
%find_lang ktouch	--with-kde
%find_lang kturtle	--with-kde
%find_lang kwordquiz	--with-kde
%find_lang marble	--with-kde
%find_lang parley	--with-kde
%find_lang rocs		--with-kde
%find_lang step		--with-kde

%post marble -p /sbin/ldconfig
%postun marble -p /sbin/ldconfig

%post kiten -p /sbin/ldconfig
%postun kiten -p /sbin/ldconfig

%post kalgebra -p /sbin/ldconfig
%postun kalgebra -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kvtml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSatLib.so
%attr(755,root,root) %{_libdir}/libkeduvocdocument.so
%attr(755,root,root) %{_libdir}/libscience.so
%attr(755,root,root) %{_libdir}/libkdeeduui.so
%attr(755,root,root) %{_libdir}/libanalitza.so
%attr(755,root,root) %{_libdir}/libanalitzagui.so
%attr(755,root,root) %{_libdir}/libavogadro-kalzium.so
%attr(755,root,root) %{_libdir}/libkiten.so
%attr(755,root,root) %{_libdir}/libmarblewidget.so
%attr(755,root,root) %{_libdir}/libcompoundviewer.so
%{_includedir}/libkdeedu
%{_includedir}/libkiten
%{_includedir}/marble
%{_datadir}/apps/cmake/modules/*.cmake

%files blinken -f blinken.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blinken
%{_datadir}/apps/blinken
%{_datadir}/config.kcfg/blinken.kcfg
%{_desktopdir}/kde4/blinken.desktop
%{_iconsdir}/hicolor/scalable/apps/blinken.svgz
%{_iconsdir}/hicolor/*x*/apps/blinken.png

%files cantor -f cantor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cantor
%attr(755,root,root) %{_libdir}/kde4/cantor_creatematrixassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_differentiateassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_eigenvaluesassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_eigenvectorsassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_integrateassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_invertmatrixassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_kalgebrabackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_maximabackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_nullbackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_plot2dassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_plot3dassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_runscriptassistant.so
%attr(755,root,root) %{_libdir}/kde4/cantor_sagebackend.so
%attr(755,root,root) %{_libdir}/kde4/cantor_solveassistant.so
%attr(755,root,root) %{_libdir}/kde4/libcantorpart.so
%attr(755,root,root) %{_libdir}/libcantorlibs.so
%attr(755,root,root) %{_libdir}/libcantorlibs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcantorlibs.so.?
%attr(755,root,root) %{_libdir}/libcantor_config.so
%{_desktopdir}/kde4/cantor.desktop
%{_desktopdir}/kde4/cantor_part.desktop
%{_datadir}/apps/cantor
%{_datadir}/apps/cantorpart
%{_datadir}/config.kcfg/cantor.kcfg
%{_datadir}/config.kcfg/cantor_libs.kcfg
%{_datadir}/config.kcfg/maximabackend.kcfg
%{_datadir}/config.kcfg/sagebackend.kcfg
%{_datadir}/config/cantor.knsrc
%{_iconsdir}/hicolor/16x16/apps/cantor.png
%{_iconsdir}/hicolor/32x32/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/cantor.png
%{_iconsdir}/hicolor/48x48/apps/maximabackend.png
%{_iconsdir}/hicolor/48x48/apps/rbackend.png
%{_iconsdir}/hicolor/48x48/apps/sagebackend.png
%{_iconsdir}/oxygen/22x22/actions/pointer.png
%dir %{_datadir}/kde4/services/cantor
%{_datadir}/kde4/services/cantor/creatematrixassistant.desktop
%{_datadir}/kde4/services/cantor/differentiateassistant.desktop
%{_datadir}/kde4/services/cantor/eigenvaluesassistant.desktop
%{_datadir}/kde4/services/cantor/eigenvectorsassistant.desktop
%{_datadir}/kde4/services/cantor/integrateassistant.desktop
%{_datadir}/kde4/services/cantor/invertmatrixassistant.desktop
%{_datadir}/kde4/services/cantor/kalgebrabackend.desktop
%{_datadir}/kde4/services/cantor/maximabackend.desktop
%{_datadir}/kde4/services/cantor/nullbackend.desktop
%{_datadir}/kde4/services/cantor/plot2dassistant.desktop
%{_datadir}/kde4/services/cantor/plot3dassistant.desktop
%{_datadir}/kde4/services/cantor/runscriptassistant.desktop
%{_datadir}/kde4/services/cantor/sagebackend.desktop
%{_datadir}/kde4/services/cantor/solveassistant.desktop
%{_datadir}/kde4/servicetypes/cantor_assistant.desktop
%{_datadir}/kde4/servicetypes/cantor_backend.desktop
#%{_kdedocdir}/en/cantor

%files rocs -f rocs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rocs
%{_desktopdir}/kde4/rocs.desktop
%{_datadir}/apps/rocs
%{_datadir}/config.kcfg/rocs.kcfg
%{_iconsdir}/hicolor/*x*/actions/rocs*.png
%{_kdedocdir}/en/rocs

%files kalzium -f kalzium.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalzium
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kalzium.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_didyouknow.so
%attr(755,root,root) %{_libdir}/kde4/concentrationCalculator.so
%attr(755,root,root) %{_libdir}/kde4/gasCalculator.so
%attr(755,root,root) %{_libdir}/kde4/nuclearCalculator.so

%attr(755,root,root) %ghost %{_libdir}/libavogadro-kalzium.so.?
%attr(755,root,root) %{_libdir}/libavogadro-kalzium.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcompoundviewer.so.?
%attr(755,root,root) %{_libdir}/libcompoundviewer.so.*.*.*

%dir %{_libdir}/avogadro-kalzium/
%dir %{_libdir}/avogadro-kalzium/colors
%attr(755,root,root) %{_libdir}/avogadro-kalzium/colors/libchargecolor.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/colors/libdistancecolor.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/colors/libindexcolor.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/colors/libresiduecolor.so

%dir %{_libdir}/avogadro-kalzium/engines
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libaxesengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libcartoonengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libdipoleengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libforceengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libhbondengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/liblabelengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/liborbitalengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/liboverlayengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libpolygonengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libribbonengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libringengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libsimplewireengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libsphereengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libstickengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libsurfaceengine.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/engines/libwireengine.so

%dir %{_libdir}/avogadro-kalzium/tools
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libaligntool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libautoopttool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libautorotatetool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libbondcentrictool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libclickmeasuretool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libdrawtool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libmanipulatetool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libnavigatetool.so
%attr(755,root,root) %{_libdir}/avogadro-kalzium/tools/libselectrotatetool.so

# XXX: ugly dir deps? -> devel?
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kalziumuiwidgets.so

%{_datadir}/apps/desktoptheme/default/widgets/chalkboard.svg
%{_datadir}/apps/kalzium
%{_datadir}/config/kalzium.knsrc
%{_datadir}/config.kcfg/kalzium.kcfg
%{_datadir}/kde4/services/plasma-dataengine-kalzium.desktop
%{_datadir}/kde4/services/plasma_didyouknow.desktop
%{_datadir}/kde4/services/concentrationCalculator.desktop
%{_datadir}/kde4/services/gasCalculator.desktop
%{_datadir}/kde4/services/nuclearCalculator.desktop
%{_desktopdir}/kde4/kalzium.desktop
%{_iconsdir}/hicolor/scalable/apps/kalzium.svgz
%{_iconsdir}/hicolor/*x*/apps/kalzium.png
%{_mandir}/man1/kalzium.1*

%files kanagram -f kanagram.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kanagram
%{_datadir}/apps/kanagram
%{_datadir}/config/kanagram.knsrc
%{_datadir}/config.kcfg/kanagram.kcfg
%{_desktopdir}/kde4/kanagram.desktop
%{_iconsdir}/hicolor/scalable/apps/kanagram.svgz
%{_iconsdir}/hicolor/*x*/apps/kanagram.png

%files kbruch -f kbruch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_datadir}/apps/kbruch
%{_datadir}/config.kcfg/kbruch.kcfg
%{_desktopdir}/kde4/kbruch.desktop
%{_iconsdir}/hicolor/scalable/apps/kbruch.svgz
%{_iconsdir}/hicolor/*x*/apps/kbruch.png
%{_mandir}/man1/kbruch.1*

%files kgeography -f kgeography.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeography
%{_datadir}/apps/kgeography
%{_datadir}/config.kcfg/kgeography.kcfg
%{_desktopdir}/kde4/kgeography.desktop
%{_iconsdir}/hicolor/scalable/apps/kgeography.svgz
%{_iconsdir}/hicolor/*x*/apps/kgeography.png

%files khangman -f khangman.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/khangman
%{_datadir}/apps/khangman
%{_datadir}/config.kcfg/khangman.kcfg
%{_datadir}/config/khangman.knsrc
%{_desktopdir}/kde4/khangman.desktop
%{_iconsdir}/hicolor/scalable/apps/khangman.svgz
%{_iconsdir}/hicolor/*x*/apps/khangman.png
%{_mandir}/man6/khangman.6*

%files kig -f kig.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pykig.py
%attr(755,root,root) %{_libdir}/kde4/kigpart.so
%attr(755,root,root) %{_bindir}/kig
%{_desktopdir}/kde4/kig.desktop
%{_datadir}/kde4/services/kig_part.desktop
%{_datadir}/apps/kig
%{_iconsdir}/hicolor/*x*/apps/kig.png
%{_iconsdir}/hicolor/scalable/apps/kig.svgz
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kig.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-kig.svgz
%{_mandir}/man1/kig.1*

# XXX pulls kate dep via dir. subpackage?
%{_datadir}/apps/katepart/syntax/python-kig.xml

%files kiten -f kiten.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%attr(755,root,root) %{_bindir}/kitenradselect
%attr(755,root,root) %ghost %{_libdir}/libkiten.so.4
%attr(755,root,root) %{_libdir}/libkiten.so.*.*.*
%{_datadir}/apps/kiten
%{_datadir}/apps/kitenradselect
%{_datadir}/config.kcfg/kiten.kcfg
%{_desktopdir}/kde4/kiten.desktop
%{_iconsdir}/hicolor/scalable/apps/kiten.svgz
%{_iconsdir}/hicolor/*x*/apps/kiten.png

%files klettres -f klettres.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klettres
%{_datadir}/apps/klettres
%{_datadir}/config.kcfg/klettres.kcfg
%{_datadir}/config/klettres.knsrc
%{_desktopdir}/kde4/klettres.desktop
%{_iconsdir}/hicolor/scalable/apps/klettres.svgz
%{_iconsdir}/hicolor/*x*/apps/klettres.png

%files kmplot -f kmplot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%attr(755,root,root) %{_libdir}/kde4/libkmplotpart.so
%{_datadir}/apps/kmplot
%{_datadir}/config.kcfg/kmplot.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.View.xml
%{_datadir}/kde4/services/kmplot_part.desktop
%{_desktopdir}/kde4/kmplot.desktop
%{_iconsdir}/hicolor/scalable/apps/kmplot.svgz
%{_iconsdir}/hicolor/*x*/apps/kmplot.png
%{_mandir}/man1/kmplot.1*

%if 0
%files kpercentage -f kpercentage.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpercentage
%{_datadir}/apps/kpercentage
%{_desktopdir}/kde4/kpercentage.desktop
%{_iconsdir}/hicolor/scalable/apps/kpercentage.svgz
%{_iconsdir}/hicolor/*x*/apps/kpercentage.png
%endif

%files kstars -f kstars.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhtmesh.a
#%attr(755,root,root) %{_libdir}/libsbigudrv.so
#%attr(755,root,root) %{_bindir}/indiserver
#%attr(755,root,root) %{_bindir}/indi_apogee_alta
#%attr(755,root,root) %{_bindir}/indi_fli_ccd
#%attr(755,root,root) %{_bindir}/indi_lx200basic
#%attr(755,root,root) %{_bindir}/indi_lx200generic
#%attr(755,root,root) %{_bindir}/indi_celestron_gps
#%attr(755,root,root) %{_bindir}/indi_orion_atlas
#%attr(755,root,root) %{_bindir}/indi_skycommander
#%attr(755,root,root) %{_bindir}/indi_intelliscope
#%attr(755,root,root) %{_bindir}/indi_fli_pdf
#%attr(755,root,root) %{_bindir}/indi_robofocus
#%attr(755,root,root) %{_bindir}/indi_trutech_wheel
#%attr(755,root,root) %{_bindir}/indi_fli_wheel
#%attr(755,root,root) %{_bindir}/indi_meade_lpi
#%attr(755,root,root) %{_bindir}/indi_sbig_ccd
#%attr(755,root,root) %{_bindir}/indi_v4l_generic
#%attr(755,root,root) %{_bindir}/indi_v4l_philips
%attr(755,root,root) %{_bindir}/kstars
%{_desktopdir}/kde4/kstars.desktop
%{_datadir}/config.kcfg/kstars.kcfg
%{_datadir}/config/kstars.knsrc
%{_datadir}/apps/kstars
%{_iconsdir}/hicolor/*x*/apps/kstars.png
%{_iconsdir}/hicolor/scalable/apps/kstars.svgz

%files ktouch -f ktouch.lang
%defattr(644,root,root,755)
%{_datadir}/apps/ktouch
%{_desktopdir}/kde4/ktouch.desktop
%attr(755,root,root) %{_bindir}/ktouch
%{_datadir}/config.kcfg/ktouch.kcfg
%{_iconsdir}/hicolor/*x*/apps/ktouch.png
%{_iconsdir}/hicolor/scalable/apps/ktouch.svgz
%{_mandir}/man1/ktouch.1*

%files kturtle -f kturtle.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kturtle
%{_desktopdir}/kde4/kturtle.desktop
%{_datadir}/apps/kturtle
%{_iconsdir}/hicolor/*x*/apps/kturtle.png
%{_iconsdir}/hicolor/scalable/apps/kturtle.svgz

%files kwordquiz -f kwordquiz.lang
%defattr(644,root,root,755)
%{_datadir}/apps/kwordquiz
%attr(755,root,root) %{_bindir}/kwordquiz
%{_desktopdir}/kde4/kwordquiz.desktop
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_datadir}/config/kwordquiz.knsrc
%{_iconsdir}/hicolor/*x*/apps/kwordquiz.png

%files libkdeeducore
%defattr(644,root,root,755)
%{_datadir}/apps/libkdeedu
%attr(755,root,root) %ghost %{_libdir}/libSatLib.so.?
%attr(755,root,root) %{_libdir}/libSatLib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdeeduui.so.?
%attr(755,root,root) %{_libdir}/libkdeeduui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkeduvocdocument.so.?
%attr(755,root,root) %{_libdir}/libkeduvocdocument.so.*.*.*
#%attr(755,root,root) %{_libdir}/libsbigudrv.so.1
#%attr(755,root,root) %{_libdir}/libsbigudrv.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libscience.so.?
%attr(755,root,root) %{_libdir}/libscience.so.*.*.*

%files kalgebra -f kalgebra.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libanalitza.so.?
%attr(755,root,root) %{_libdir}/libanalitza.so.*.*.*
%attr(755,root,root) %{_libdir}/libanalitzagui.so.?
%attr(755,root,root) %{_libdir}/libanalitzagui.so.*.*.*
%attr(755,root,root) %{_bindir}/kalgebra
%{_desktopdir}/kde4/kalgebra.desktop
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kalgebra.so
%{_datadir}/kde4/services/kalgebraplasmoid.desktop
%{_iconsdir}/hicolor/*x*/apps/kalgebra.png
%attr(755,root,root) %{_bindir}/calgebra

%files marble -f marble.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geodatatest
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/tilecreator

%attr(755,root,root) %ghost %{_libdir}/libmarblewidget.so.4
%attr(755,root,root) %{_libdir}/libmarblewidget.so.*.*.*

%attr(755,root,root) %{_libdir}/kde4/libmarble_part.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_worldclock.so

%dir %{_libdir}/kde4/plugins/marble
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CompassFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MapScaleFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NavigationFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CrosshairsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GeoRendererPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpsdPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GraticulePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OverviewMap.so
#%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OsmAnnotatePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Photo.so
#%attr(755,root,root) %{_libdir}/kde4/plugins/marble/QHttpNetworkPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/QNamNetworkPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/StarsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Weather.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Wikipedia.so

%dir %{_datadir}/apps/marble_part
%{_datadir}/apps/marble
%{_datadir}/apps/marble_part/marble_part.rc
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kde4/services/marble_part.desktop
%{_datadir}/kde4/services/plasma-applet-kworldclock.desktop
%{_desktopdir}/kde4/marble.desktop
%{_iconsdir}/hicolor/*x*/apps/marble.png

%files parley -f parley.lang
%defattr(644,root,root,755)
%{_datadir}/apps/parley
#%attr(755,root,root) %{_bindir}/parleypractice
%{_iconsdir}/hicolor/*x*/apps/parley.png
%{_iconsdir}/hicolor/scalable/apps/parley.svgz
%{_iconsdir}/hicolor/scalable/apps/parley-parley.svgz
%{_iconsdir}/hicolor/scalable/apps/parley-simple.svgz
%attr(755,root,root) %{_bindir}/parley
%{_desktopdir}/kde4/parley.desktop
%{_datadir}/config/parley.knsrc
%{_datadir}/config.kcfg/parley.kcfg
%{_datadir}/config.kcfg/languagesettings.kcfg
%{_datadir}/config.kcfg/documentsettings.kcfg
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_parley.so
%{_datadir}/kde4/services/plasma_parley.desktop
%{_datadir}/apps/desktoptheme/default/widgets/parley_plasma_card.svg
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_parley.so
%{_datadir}/kde4/services/plasma-dataengine-parley.desktop

%files step -f step.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/step
%{_datadir}/apps/step
%{_datadir}/config.kcfg/step.kcfg
%{_datadir}/config/step.knsrc
%{_desktopdir}/kde4/step.desktop
%{_iconsdir}/hicolor/*/apps/step.png
# already in oxygen icons
#%{_iconsdir}/oxygen/*/actions/pointer.png
%{_iconsdir}/oxygen/*/actions/step_*.png
