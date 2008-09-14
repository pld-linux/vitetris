#
Summary:	Console based tetris clone
Summary(pl.UTF-8):	Tetris w konsoli tekstowej
Name:		vitetris
Version:	0.51
Release:	0.1
License:	BSD-like
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	7674b536021139c100600ddb992fe2dc
URL:		http://victornils.net/tetris/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vitetris is a terminal-based Tetris clone. Gameplay is much like the
early Tetris games by Nintendo.

- Configurable keys
- Highscore table
- Two-player mode with garbage
- Network play
- Joystick (gamepad) support on Linux or with Allegro

%description -l pl.UTF-8
vitetris jest konsolowym klonem klasycznej gry Tetris. Styl gry
przypomina wczesne gry typu Tetirs na Nintendo.

%prep
%setup -q

%build
./configure
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},/var/games}
install tetris $RPM_BUILD_ROOT%{_bindir}/vitetris
touch $RPM_BUILD_ROOT/var/games/vitetris-hiscores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vitetris
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/vitetris-hiscores
%doc changes.txt README licence.txt
