Summary:	Console based tetris clone
Summary(pl.UTF-8):	Tetris w konsoli tekstowej
Name:		vitetris
Version:	0.56
Release:	0.1
License:	BSD-like
Group:		Applications/Games
Source0:	http://victornils.net/tetris/%{name}-%{version}.tar.gz
# Source0-md5:	fc66ca3f90a95e9b270d68720dfe83ea
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
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
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix="%{_prefix}"
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install hiscores
install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/vitetris-hiscores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt licence.txt
%attr(755,root,root) %{_bindir}/vitetris
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/vitetris-hiscores
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
