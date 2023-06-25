import constants, entities, functions
gameboook = {}
def get_translation(translation):
    while True:
        gameboook = {
            'en':
                {"xxx": "",
                 "00a": f"\r{constants.def_txt_clr}While wandering through the underground, you will find different types of weapons and items. \
                \nRemember that - except for the sword - each weapon can be used only once. \
                \nSimilarly, the found items are for single use. \
                \nYou can take one bottle of elixir with you.",
                 "00b": "Hey, Brave One! \
                \n\
                \nThey say about you that icy water flows in your veins instead of blood, \
                \nand your muscles are made of the noblest steel? \
                \nIf so, look towards the setting sun. \
                \nThere, at the borders of the kingdom of Almanhagor, the uncharted Underground begins. \
                \nOnly you can unveil its Great Secret. Go forth!",
                 "01": "The entrance to the underground is wide, overgrown with grass and lush bushes. \
                \nYou adjust your clothing and equipment. \
                \nLight your lantern! You enter the corridor. It is tall, and you don't have to stoop. \
                \nIt leads straight to the north. Soon, you reach a crossroads. \
                \nIt has the shape of the letter T. The branches lead west, east, and south (where you came from)."
                 },
            'pl':
                {"xxx": "",
                 "00a": f"\r{constants.def_txt_clr}Wędrując po podziemiach będziesz znajdował inne rodzaje broni i przedmioty.\
                \nPamiętaj, że - poza mieczem - każda broń może być wykorzystana tylko raz.\
                \nPodobnie, znajdowane przedmioty są jednorazowego użytku.\
                \nMożesz zabrać ze sobą jedną butelkę eliksiru.",

                 "00b": "Hej, Śmiałku!\
                \n\
                \nTo o Tobie mówią, że w Twoich żyłach zamiast krwi płynie lodowata woda,\
                \na twoje mięśnie są z najszlachetniejszej stali?\
                \nJeśli tak, spójrz w stronę zachodzącego słońca.\
                \nTam, na rubieżach królestwa Almanhagor, rozpoczynają się niezbadane Podziemia.\
                \nTylko Ty możesz wydrzeć ich Wielką Tajemnicę. Ruszaj!",

                 "01": 'Wejście do podziemi jest szerokie, obrośnięte trawą i bujnymi krzewami.\
                \nPoprawiasz ubranie i ekwipunek.\
                \nZapal latarnię! Wchodzisz do korytarza. Jest wysoki, nie musisz się schylać.\
                \nProwadzi prosto na północ. Wkrótce dochodzisz do skrzyżowania.\
                \nMa ono kształt litery T. Odnogi prowadzą na zachód, wschód i południe (skąd przyszedłeś).',

                 "02": "Kopnij drzwi. Otwierają się i uderzają o skałę.\
                \nWchodzisz do środka z mieczem gotowym do zadania ciosu.\
                \nNa pewno potwór nigdzie się nie ukrywa. Czuje się zbyt potężny.\
                \nTak, widzisz go przed sobą. Stoi na szeroko rozstawionych nogach.\
                \nOn też ma miecz. Czub wbił się w piasek. Opiera dłonie na rękojeści.\
                \nCzeka. Ty nie czekaj! Jeśli masz hełm, załóż go koniecznie, zapewni ci +3W na czas trwania tej walki.",

                 "03": "Twoja cierpliwość - a szczególnie zapasy złota - są na wyczerpaniu.\
                \nA może inaczej? Starzy mieszkańcy podziemi mówią, że Smok ma swoje słabe strony.\
                \nSzczególnie słaba jest jego lewa strona, gdzie nosi wór na pieniądze i złoto.\
                \nMoże by tak spróbować jeszcze raz, płacąc ponad taryfę (13 sztuk złota)?",

                 "04": "KRASNOLUDY prowadzą cię do stołu. Przynoszą na półmiskach czystą, zieloną sałatę.\
                \nStawiają pucharki. Rozlewasz napój. Kątem oka spostrzegasz,\
                \nże dwa KRASNOLUDY wychodzą z pokoju wschodnimi drzwiami.\
                \nRozpinasz rzemień, ukradkiem wyciągasz miecz i kładziesz go przed sobą na stole.\
                \nZapada cisza. KRASNOLUDY bacznie cię obserwują.\
                \nTy patrzysz im prosto w oczy. Milczenie przeciąga się",

                 "05": "Lubisz walkę? Tak? To wspaniale. Przyjrzyj się więc dokładnie.\
                \nOd lewej stoją: SZKIELET, ZOMBI i LUDOJAD. Wystarczy?",

                 "06": "Możesz rozejrzeć się po komnacie. Ech, toż to prawdziwa zbrojownia krasnali ziemnych.\
                \nNa ścianach wiszą tarcze, niektóre ciężkie, u góry i u dołu zakończone ostrymi szpicami,\
                \ninne ozdobne, obite czerwono-złotymi płytkami: są też lekkie tarcze skórzane.\
                \nNa stojaku błyszczą miecze. Te najdłuższe, cienkie, to jedyna skuteczna broń przeciw wiedźmom.\
                \nMiecze kamienne o gładkim brzeszczocie i ostrym jak igła czubie przeznaczone są do walki z płazurami.\
                \nNie wykonuje się nimi zamachów, lecz spuszcza z góry, by przeszywały cielska tych potworów.\
                \nPrzy samej ziemi widzisz poustawiane w rzędzie malutkie mieczyki gremlinów, krasnali ziemnych.\
                \nGdybyś widział jaki potrafią robić z nich użytek!\
                \nNa wschodniej ścianie wiszą drewniane półki zastawione całą kolekcją hełmów.\
                \nSą hełmy do pojedynków turniejowych, wyściełane żółtą trawą, są ciężkie hełmy z podnoszoną przyłbicą.\
                \nNa najwyższej półce stoją trzy - chyba - garnki. Nie, to są hełmy\
                \ndo walki w pomieszczeniach albo korytarzach wypełnionych żrącym gazem.\
                \nCzubkiem miecza podrzucasz jakieś skórzane płaty.\
                \nTo czapa, którą okrutne potwory zakładają na łeb torturowanym przez siebie istotom.\
                \nRozglądasz się dalej. Pod ścianami stoi, albo leży mnóstwo broni.\
                \nNawet nie wiesz komu i do czego służy. Widzisz ciężki młot na drewnianym stylisku,\
                \nzapewne zdobyty kiedyś na goblinach, a także kościany kordelas w skórzanym futerale.\
                \nMożesz zabrać dwie rzeczy.",

                 "07": "'Może ma Pan na składzie coś, co mógłbym ofiarować w prezencie?' - mówisz.\
                \n'Jak mógłbym nie mieć? Jestem zawsze przygotowany na takie zachcianki.\
                \nMam uroczy drewniany pal i słój żrącego pyłu. Zapakować ze wstążeczką?'.",

                 "08": "Zaglądasz do komnaty. Drzwi lekko się uchylają. Co widzisz?\
                \nJakiś dziwnystwór biega jak oszalały od ściany do ściany. Nie wygląda groźnie.\
                \nZa pas, wkieszenie, do cholew powtykane ma rozmaitej długości i różnego gatunku kości.\
                \nWchodzisz do środka. 'Czemu tak biegasz, biedaku?' - pytasz.\
                \n-'O, panie, co jaim zrobiłem? Taki raban o tych parę kostek! Moi bracia, gobliny upolowali kilkakocmołuchów.'\
                \nJak pewnie wiesz, kocmołuchy to największy przysmak goblinów. Niemogłem sobie odmówić.\
                \nPodkradłem się i gwizdnąłem kilka kostek. Siadłem tu, byje sobie zjeść,\
                \na te bestie wyśledziły mnie i zaraz tu wpadną. O, już biegną.'\
                \nIgoblin znów zaczyna szaleć. Bierzesz go za ramię i stajesz na środku komnaty.\
                \nZa chwilę w drzwiach pojawia się stado goblinów.",

                 "09": "Przygotowujesz się, by walnąć KRASNALA drewnianym palem. On spostrzega to.\
                \n'Och, co za piękny pal' - mówi - 'Sprzedaj mi go za 20 sztuk złota.",

                 "10": "KRASNOLUDY zapraszają cię, byś usiadł przy stole. Uśmiechają się.\
                \n'Nareszcie jakiś kulturalny potwór' - mówią. 'Wszyscy tylko wpadają tu, wyrywają główki\
                \nsałaty i zwiewają. Ale nie mamy im tego za złe. Przynajmniej komuś przyda się\
                \nnasze warzywko, he, he'. Zamyśliłeś się chwilę nad tym 'he, he', a tu już\
                \nKRASNOLUDY zaczynają snuć opowieści. Niewielu z nich zapuszczało się\
                \nkiedykolwiek w dalsze rejony podziemi. Ci, którzy wrócili, mówią,\
                \nże najstraszniejszą rzeczą którą można spotkać jest ogień. Błąka się też po\
                \nlabiryncie tłusty Smok. Podobno jest bardzo groźny, choć niektórzy powiadają,\
                \nże jest przekupny.\
                \n\
                \nSłuchasz tych opowieści, ale ciągle coś nie daje ci spokoju.\
                \n   ///   Jeśli szedłeś ścieżką przez środek komnaty /../../../",

                 "11": "Przejście stoi otworem. Do tej komnaty nie ma żadnych drzwi.\
                \nWchodzisz więc śmiało.\
                \n'Cześć' - jedno słowo a ty nieruchomiejesz.\
                \n'Cześć, Śmiałku, he, he' - w rogu komnaty siedzi mały, pomarszczony stwór.\
                \n'Pić ci się chce? Weź sobie wody. Dobra, chłodna woda. Palce lizać i obgryzać'.\
                \nNa środku komnaty stoi kamienna fontanna. Woda otacza figurkę jakiejś niezwykłej istoty.\
                \nZ pyszczka wycieka jej mały strumyk wody. '...Są prawdziwe skarby. Chcesz skosztować wody?\
                \nTo dobra chłodna woda'. Stoisz jak wryty. Ten mały śmieszny stwór zabił ci ćwieka.\
                \nCałkiem straciłeś rezon. No, decyduj się:",

                 "12": "Wyjmujesz zaczarowany szmaragd. Ból rozrywa ci plecy, pęka skórzana kurtka.\
                \nZ pleców wyrastają ci szerokie, sinoszare skrzydła. Unosisz się. Lądujesz na\
                \nwymarzonym brzegu przepaści. Czar pryska.",

                 "13": "Nie musisz się rozglądać. Od razu powiem ci wszystko. W tej komnacie czai się\
                \nWILKOŁAK. Wie, że tu jesteś. Robisz kilka kroków w mrok Za wyłomem skalnym\
                \ndostrzegasz świecący punkt. Ukradkiem sięgasz po miecz. Robisz kolejne kroki.\
                \nTeraz już są dwa punkty. Łoskot. Zza skały wyskakuje on. W smudze światła,\
                \nktóra pada przez uchylone drzwi do pieczary, widzisz tylko białe kły i zielone oczy.\
                \nBłyskawicznie chwytasz oburącz swój miecz. Robisz zamach...\
                \ni zastygasz nieruchomo. Zielone ślepia paraliżują twe ciało",

                 "14": "Możesz wyjść północnymi drzwiami - patrz 197, albo wschodnimi - patrz 39.",

                 "15":
                     "Jeśli rezygnuiesz z przepłynięcia jeziora - patrz 241, Natomiast jeżeli decydujesz się podjqć próbę przepłynięcia jeziora, zapisz numer niniejszego paragrafu i patrz 113.",

                 "16a": "Wychodzisz na korytarz. Po pewnym czasie skręca on na południe. W tym samym\
                \nmiejscu możesz usiąść i zjeść Prowiant.",

                 "16b": "Ruszasz dalej. Idziesz na południe do czasu, gdy tunel skręca na znowu zachód.\
                \nW odległości dwudziestu kroków widzisz przed sobą wejście do komnaty.",

                 "17": "Jeśli chcesz zobaczyć co za nimi iest - patrz 265, jeśli wolisz się wycofać - patrz 50.",

                 "18": "Wchodzisz do małej pieczary, przylegającej do komnaty. Za tobą trzy ZŁE.\
                \nStaruszek został w pokoju. Za wyłomem skalnym widzisz przykutego do skały\
                \ngremlina. Biedaczysko ledwie zipie. ZŁY bierze cię za ramię i odprowadza na\
                \nodległość dziesięciu kroków od gremlina. Daje ci w garść sześć strzałek. ZŁY też\
                \nma sześć. Pokazuje palcem w stronę zakutego gremlina. To w niego należy celować!\
                \nChcesz grać?",

                 "19": "KRASNOLUDY żegnają cię serdecznie i wręczają na drogę dwie główki sałaty.\
                \nOdprowadzają cię do wschodnich drzwi.",

                 "20": "Po długim marszu dochodzisz do jakiejś wielkiej jaskini.\
                \nNie, to raczej bezkresna równina. Zapewne sławetne Szalone Pola.\
                \nSłyszysz jakiś hałas. Co sił wnogach biegniesz na zachód.\
                \nJednak potwory dopadają cię.",

                 "21": "Jeśli chcesz zobaczyć co jest za drzwiami - patrz 332, jeśli nie - zawracasz i patrz 212.",

                 "22": "To chyba juz kres twej wędrówki. Tak ślicznej komnaty ieszcze nie widziałeŚ.\
                \nWszędzie jasno, unosi się zielonkawa mgiełka. Posadzka jeszcze gładsza niż nad przepaścią.\
                \nNa podłodze siedzi jakiś ludek. Ah, to prawdziwy KRASNAL bawi się smoczkiem, nakręcanym,\
                \nz ruchomymi nogami i czerwonym językiem, który mu się co chwilę wysuwa. JeŚli masz\
                \nblaszanego motyla, możesz odpocząć i pobawić się z KRASNALEM - patrz 321.\
                \nJeśli masz szmaragd, możesz pokazać go KRASNALOWI - patrz 187. Tylko wtedy,\
                \ngdy masz drewniany pal, możesz próbować postraszyć albo nawet zaatakowac KRASNALA -patrz 9.\
                \nJeżeli masz więcej niż,iedną z wymienionych rzeczy, musisz wybrac tylko jedną możliwość",

                 "23": "Drzwi do skarbca stoia przed toba... otworem? o, nie! są zamknięte.\
                \nWidzisz dwa zamki. Jeśli masz przynaimniej dwa numerowane kluczyki,\
                \nmożesz otworzyć nimi drzwi - patrz 185. Jeśli nie masz choć dwóch kluczy,\
                \ntu kończy się twoja Wyprawa. A było tak blisko!",

                 "24": "Rzuć raz kostką. Jeśli wy|osujesz 1, 2, 3 - twoja broń\
                \nokaże się skutecznym narzędziem w walce z ROBALAMI - patrz 58.\
                \nJeŚli wylosujesz 4, 5, 6, nic z tego - patrz 168.",

                 "25": "Na kamieniu siedzi stary człowiek. Radzi ci iść na zachód,\
                \na później na kilku najbliższych skrzyżowaniach skręcać w prawo.",

                 "26": "Za celne trafienie każdego grubasa dostajesz 5 sztuk złota. Patrz 171.",

                 "27": "Korytarz prowadzi prosto na północ. Po drodze możesz zjeść Prowiant.\
                \nZaczyna się rozszerzać, powiększać, aż wychodzisz na bezkresną równinę, To szalone Pola.\
                \nLepiej się tam nie zapuszczaj. Ale... czy słyszysz to dudnienie? To na pewno potwory.\
                \nPatrz 238. JeŚli je pokonasz albo wycofasz się w trakcie walki - patrz 316.\
                \nZapisz ten numer, bo zgubisz drogę.",

                 "28": "Podnieś wielki kamień leżący przy ścianie.",

                 "29": f"Potykasz się na kamyku. Miecz brzęknął o skałę. {entities.entity_116.name} podnosi głowę.\
                \nZauważył cię. Rzuca się do walki.",

                 "30": "SSS. Jeśli masz S - patrz 159. JeŚli nie masz S - patrz 342.",

                 "31": "Poświeć latarnią niżej. Rozgarnij mieczem to padło. A widzisz - znalazteś 5 sztuk ztota!",

                 "32": f"Wyczerpany siadasz pod skałą. Możesz zjeść coś z Prowiantu.\
                \nLedwie skończyłeś posiłek, gdy do pieczary wpadają WILKOLUDY, znacznie\
                \nsłabsze od WILKOŁAKA, ale za to są trzy. Traktujesz je jako jednego potwra i walczysz.\
                \n{entities.entity_032.name}\
                \nJeśli zwyciężyłeś - patrz 275.",

                 "33": "Jeszcze trochę i będziesz na skrzyżowaniu.\
                \nIdziesz na: . północ - patrz 293, na wschód - patrz 188, na południe - patrz 247",

                 "34": "Ujawniasz swe odkrycie: drzwi w północnej ścianie. Nie robi to na nich wrażenia.\
                \nMówisz. że chcesz zobaczyć, co za nimi jest. Nie protestują.. Wstajesz od stołu i wzdłuż ściany\
                \ndochodzisz do sekretnych drzwi. Jeden z KRASNOLUDÓW przekręca ukrytą w ziemi gałkę.\
                \nDrzwi otwierają się. Wchodzisz - patrz 128",

                 "35": "Płacisz wedtug taryfy (10 sztuk ztota). On rozkracza się nad rozpadliną. Podstawia ci ogon.\
                \nWchodzisz. Zapewne zaraz przeniesie cię na druga stronę wąwozu. Ale... Smok ma swoie humory. Często mu się zmieniają.\
                \nWłaśnie teraz obłapiasz jego ogon Wiszac nad czerwoną otchłanią. SSS. Jeśli masz S, przechodzisz na drugi brzeg - patrz 186.\
                \nJeśli nie masz S, Smok zrzuca cię z powrotem na krawędz skalną - patrz 158",

                 "36": "SSS. Jeśli masz S - patrz 152. .jeśli nie masz S - patrz 176",

                 "37":
                     "Jaka tarczę wybierasz: metalową, paradną, czy skórzaną? Wpisz swój wybór na listę ekwipunku - patrz 324.",

                 "38": "Korytarz prowadzi najpierw na północ, a pózniej łagodnym łukiem skręca ku wschodowi.\
                \nRozszerza się nieco i kończy schodami biegnącymi w dół. Stajesz przed drzwiami pokrytymi wyszukanymi ozdobami.\
                \nCzy byłeś iuż za tymi drzwiami? Jeśli tak - patrz 167, jeśli nie - patrz 328.",

                 "39": "Dochodzisz do skrzyżowania. Jego odnogi prowadzą na:",

                 "40":
                     "Czy będziesz polegał tylko na kartach? - patrz 334, czy też będziesz korzystał ze swoiego SZCZĘŚCIA? - patrz 62",

                 "41": "Udało ci się zrobić tylko parę kroków a tu korytarz zupełnie zatarasowany masą kamieni i piasku.\
                \nSpróbuj tupnac noga. Stare gremliny mówią, że to jest sposób na takie zawalidrogi. SSS. Jeśli masz S - góra skał\
                \nwpada gdzieŚ w przepaść, możesz iść da|ej - patrz 348. Jeśli nie masz S - musisz wrócić - oatrz 221,",

                 "42": "Mówią o nim BARBARZYŃCA. czy słusznie? Kto wie? Gdy tak siedzi na ławie z wyciągniętymi nogami i rękami założonymi\
                \nna piersiach, nie wyglada groźnie. Cicho chrapie. Walisz mieczem w ścianę. Co jest? Ocknął się. Wchodzisz teraz do komnaty\
                \ni pokazujesz na drzwi po przeciwnej, zachodniej stronie. Otwieraj szybko tamte drzwi - pokazuiesz mu końcem miecza.\
                \nSam sobie otwórz - rechoce - Klucz jest w zamku: Istotnie. Podchodzisz do drzwi. obawiając się zasadzki,\
                \nnie dotykasz ręką klucza, lecz wsadzasz czub miecza w oko klucza i próbujesz przekręcic. Nic z tego. \
                \nNic z tego...- ryczy BARBARZYŃCA - Zaklęcie znasz? Jeśli nie znasz, to lepiej się stąd wynoś!\
                \nNo, właśnie, pamiętasz zaklęcie ze starej księgi gremlinów? Zaraz, a może ty wcale nie widziałeś tej księgi\
                \nTak czy owak, jeśli nie znasz zaklęcia, to koniec z tobą, bratku. spróbuj jeszcze raz, od samego początku.\
                \nJeśli wydaje ci się, że pamiętasz zaklęcie, powtórz je, Teraz zairzyj do paragrafu 122. Jeśli zapamiętałeś prawidłowo - patrz 376.\
                \nJeżeli zrobiłeś choćby najmniejszy błąd, kończysz przygodę. Jej dalsze prowadzenie w takiej sytuacji nie jest godne prawdziwego Śmiałka.",

                 "43": "Musisz wrócić tędy, którędy przyszedłeś, aż znaidziesz się na drugim końcu przepaści. Po drodze z nikim nie walczysz,\
                \nniczego nie kupujesz, niczego nie zabierasz. Musisz spróbować innego wyjścia. Wymienione są w paragrafie 186.",

                 "44": "Idziesz na wschód. Widzisz przed sobą solidne drzwi.\
                \nPróbujesz je otworzyć. Nie ustępują...",

                 "45": "Kierujesz się w stronę fontanny. Nabierasz wody. Jest zaczarowana.\
                \nChowasz naczynie do plecaka. Spostrzegasz, że fontanna jest już pusta.",

                 "46":
                     "Wypatrujesz, jak wyjść z północnego brzegu pieczary. Widzisz niewielki otwór. Ruszasz w jego stronę i przeciskasz się z trudem. Patrz 53",

                 "47": "Przeszedłeś zaledwie kilkanaście kroków i korytarz skręca w prawo, a zaraz potem kończy się. Możesz usiąść i sokojnie zjeść Prowiant.\
                \nPotem wracaj do skrzyźownia i idż na północ - patrz 191",

                 "48": "Otwierasz plecak i sięgasz po naczvnie, by przesypać skarb. W tej samej chwili złoto rozpryskuje się we wszystkie strony,\
                \na wazy przemieniają się w dwa potężne, skrzydlate DEMONY, które wznoszą się i siadają na slnym występie. Możesz zaatakować je - patrz 169,\
                \nalbo wziąć się do zbierania rozsypanego złota - patrz - 33.",

                 "49": "Możesz wziąc tę księgę ze sobą (wpisz na listę ekwipunku) albo ją zostawić. Patrz 286.",

                 "50": "Zbliżasz się do skrzyżowania.\
                \nMożesz iść:",

                 "51":
                     "Możesz wyjść drzwiami południowi - patrz 134, albo północnymi - patrz 33. Jedne i drugie drzwi zostaw otwarte",

                 "52": "Z otworu w ścianie wystrzeliwuje strumień gryzącego gazu. Jeśli masz hełm garnkowy, nie dzieje ci się krzywda.\
                \nChoć hełm ulega zniszczeniu. Jeśli nie masz takieqo hełmu - patrz najpierw 315, a potem 274 (zapisz ten numer).",

                 "53": "Lądujesz w przestronnym chodniku. Wiedzie na północ, a po pewnym czasie skręca ostro na wschód.\
                \nRobisz kilkadziesiąt kroków i stajesz przed ciężkimi drzwiami, - Czy byłeś już tu? Jeśli tak - patrz 322, jeśli nie - patrz 299",

                 "54": "Miotasz mtotem. Trafiłeś celnie. STRAŻNIK traci 2 W, ale nadal stoi jak słup. Patrz 107.",

                 "55": "Dajesz złoto, bierzesz pal, słój albo jedno i drugie - patrz 196.",

                 "56": "Ponownie próbujesz wyważyć drzwi. Znowu bezskutecznie.",

                 "57": "Po wylądowaniu łajdak żqda całego twoiego zlota. Możesz powiedzieć, że dasz tylko tyle, ile żądał - patrz 335,\
                \nalbo że - w takim razie - nie dasz nic - patrz 91",

                 "58": "Stosujesz swą tajemną broń. Całkowicie paralizue ROBALE. Jeśli chcesz zanurzyć się między ich cielska i\
                \nponownie przeszukać basen - patrz 142, jeśli nie . patrz 320.",

                 "59": "Wchodzisz, ale niczego tu nie znajdujesz.\
            \nCzy znasz inne wyjście z tej komnaty niż to, którym właśnie wszedłeś?",

                 "60": "KRASNAL proponuje 20 sztuk złota. Akceptujesz? Tak - patrz 262, nie - patrz 338.",

                 "61": "Idziesz korytarzem. Po drodze możesz zieść Prowiant. Po pewnym czasie odchodzi od niego rozgałęzienie na północ,\
                \nale ty uparcie podążasz na zachód. Kilkanaście kroków za tym rozgałęzieniem widzisz drzwi. Otwierasz je - patrz 42.",

                 "62": "SSS. Jeśli masz S - patrz 201, Jeśli nie masz S - patrz 145",

                 "63": "Miecz nie jest skuteczną bronią przeciw WILKOŁAKOM. Jeśli masz któryś z wymienionych przedmiotów, możesz użyc go do walki:\
                \nkośc ze szkieletu przedwiecznego potwora - patrz 157\
                \nmłot goblinów - patz 346, metafowa tarcza - patrz 216,\
                \nsieć - patrz 377, pęk kluczy - patrz 181. Jeśli nie masz żadnego z tych przedmiotów, pozostaie ci tylko Ucieczka - patrz 275.",

                 "64": "Zbliżasz się do skrzyżowania. Możesz iść w każdym z czterech kierunków.\
                \nWybierz kierunek:",

                 "65": "Masz już dosyć tego miejsca? Jeśli tak - patrz 195,  jeśli nie - patrz 283.",

                 "66":
                     "Rzucasz dwiema kostkami. Pokaża ci ile sztuk złota wygrywasz. Chcesz grac dalej? - patrz 229. Nie chcesz? - patrz 19",

                 "67": "Musisz się wycofać- patrz 50.",

                 "68":
                     "Wychodzisz ze zbrojowni. Jedyne drzwi prowadzą na północ. Podążasz korytarzem aż do najbliższego skrzyżowania. Po drodze możesz usiąść i zjeść Prowiant. Patrz 212.",

                 "69a": "Sam tego chciałeś. Pod ścianą komnaty siedzą dwa koszmarne upiory.\
                \nTakie spotkanie może zakończyć się tylko walką, najpierw z jednym, a później z drugim potworem.",

                 "69b": "Ledwo pokonałeś pierwszego upiora a już zabierasz się za drugiego.",

                 "69c": "Możesz przeszukać komnatę.",

                 "70": "",

                 "71": "",

                 "72": "",

                 "73": "",

                 "74": "",

                 "75": "Wycofujesz się. Wracasz w stronę skrzyżowania. Mijasz starca.",

                 "76": "",

                 "77": "",

                 "78": "",

                 "79": "",

                 "80": "",

                 "81": "",

                 "82": "",

                 "83": "",

                 "84": "",

                 "85": "",

                 "86": "",

                 "87": "",

                 "88": "",

                 "89a": "Czubem miecza podważasz wieko pudełka. Wewnątrz są 3 sztuki złota.\
                \nMożesz je wziąć.",

                 "89b": "Rozglądasz się po kątach. Nagle słyszysz jakiś hałas.\
                \nZbierasz szybko swój ekwipunek i wybiegasz zostawiając drzwi otwarte.",

                 "90": "",

                 "91": "",

                 "92": "",

                 "93": "",

                 "94": "",

                 "95": "",

                 "96": "",

                 "97": "",

                 "98": "",

                 "99": "",

                 "100": "",

                 "101": "",

                 "102": "Dochodzisz do skrzyżowania. Korytarze rozchodzą się we wszystkich kierunkach.\
                \nWybierz kierunek:",

                 "103": "Wracasz. Mijasz skrzyżowanie. Idziesz na zachód. Po pewnym czasie widzisz\
                \nprzed sobą skrzyżowanie",

                 "104": "Dajesz motyla, bierzesz złoto i smoczek",

                 "105": "Próbujesz wyważyć drzwi. Rozpędzasz się i z całej siły uderzasz barkiem.\
                \nDrzwi ani drgnęły.",

                 "106": "Tuż za drzwiami widzisz drewniane, wyszczerbione schody prowadzące w dół.\
                \nW centralnej części pieczary znajduje się kwadratowe zagłębienie, coś jakby basen,\
                \nale pusty. Schody prowadzą właśnie na dno basenu. Posadzka wysypana jest miałkim piaskiem.\
                \nWszędzie piasek, żadnych sprzętów, kamieni, ani istot... Hejże,\
                \na co to za zgięta pała sterczy w rogu basenu? Pewnie jakiś korzeń. Nie możesz odmówić\
                \nsobie tej przyjemności: dajesz mu solidnego kopa. To, co się teraz dzieje,\
                \nprzekracza wyobrażenia. Jeśli przetrwasz i będziesz komuś opowiadał o swojej\
                \nprzygodzie, na pewno nie uwierzy. Basen przypomina teraz garnek, w którymś ktoś\
                \nmiesza gruby makaron. Ty jesteś małym ziarnkiem miotanym we wszystkie strony.\
                \nTo ROBALE, najobrzydliwsze stwory podziemnego świata. Chcą rozetrzeć cię na\
                \nproszek. Wiją swe śliskie cielska. To wyrzucają cię na powierzchnię, to znowu\
                \nprzyciskają cię do dna. Możesz bronić się mieczem. Możesz też\
                \nzastosować inną broń, czyli.. No właśnie: niektórzy mówią, że skuteczną bronią\
                \nprzeciw ROBALOM jest żrący płyn, inni że wszystkożery (wieczne głodne skorupiaki).",

                 "107": "",

                 "108": "",

                 "109": "",

                 "110": "",

                 "111": "",

                 "112": "",

                 "113": "",

                 "114": "",

                 "115": "Wybierz żeczy:",

                 "116a": f"Odbiegasz w kąt pieczary. Kamienie pryskają spod stóp.\
                \n{entities.entity_116.name} przygląda się uważnie i naciera. Musisz walczyć.",

                 "116b": "\nMożesz rozejrzeć się po pokoju.",

                 "117": "",

                 "118": "",

                 "119":
                     f"Co ta bestia tak zasłaniała? Dotykasz ściany w miejscu, o które opierał swe plecy włochaty {entities.entity_317.name}.\
                \nNagle cześć ściany uchyla się. To jest schowek! A w nim długa, ognioodporna lina z hakiem, pusta omszała flasza i skalp WILKOŁAKA.\
                \nMożesz wziąć najwyżej dwie z tych rzeczy.",

                 "120": "Idziesz na zachód. Korytarz łagodnie skręca w prawo i teraz prowadzi już na północ.\
                \nWidzisz przed sobą skrzyżowanie.",

                 "121": "",

                 "122": "",

                 "123": f"Korytarz biegnie na zachód i skręca na południe.\
                \nPrzed sobą widzisz skrzyżowanie.",

                 "124": "",

                 "125": "",

                 "126": "",

                 "127": "",

                 "128": "",

                 "129": "",

                 "130": "Korytarz ma teraz prawie pięć kroków szerokości.\
                \nIdziesz więc wygodnie. Prostujesz kości.\
                \nPrzeszedłeść zaledwie sto kroków, a tu znowu skrzyżowanie.",

                 "131": "",

                 "132": "Czy poszedłeś po wodę?",

                 "133": "",

                 "134": "",

                 "135": "",

                 "136": "Smok uprzejmie zaprasza cię na swój ogon, którym trochę - co prawda - buja\
                \nnad jamą, ale zaraz potem lądujesz po drugiej stronie",

                 "137": "",

                 "138": "",

                 "139": "",

                 "140": "",

                 "141": "",

                 "142": "",

                 "143": "",

                 "144": "",

                 "145": "",

                 "146": "Korytarz biegnie na połódnie i skręca na wschód.\
                \nPrzed sobą widzisz skrzyżowanie.",

                 "147": "",

                 "148": "",

                 "149": "",

                 "150": "",

                 "151": "",

                 "152": "",

                 "153": "Szczur to dobry znak. Twój miecz jest zaczarowany. W każdej walce, którą będziesz odtąd prowadził,\
                \nmożesz dodać 1 do siły ataku.",

                 "154": "",

                 "155": "",

                 "156": "",

                 "157": "",

                 "158": "Nie masz dosyć?",

                 "159": "",

                 "160": "Ostrożnie stawiasz kroki. Nogi ocierają się o liście dorodnej sałaty.\
                \nMijając środek pokoju dostrzegasz padającą z góry strużkę światła.\
                \nNie zdradzasz swego odkrycia. Dochodzisz do stołu",

                 "161": "",

                 "162": "",

                 "163": "",

                 "164": "",

                 "165": "",

                 "166": "",

                 "167": "",

                 "168": "",

                 "169": "",

                 "170": "Dochodzisz do skrzyżowania. Ma kształt litery T.\
                \nMożesz iść na:",

                 "171": "",

                 "172": "",

                 "173": "",

                 "174": "",

                 "175": "",

                 "176": "Zbliżasz się do skrzyżowania.\
                \nMożesz pójść na:",

                 "177": "Pod kamieniem schowana była ognista kula. Możesz ją zabrać.\
                \nWychodzisz.",

                 "178": "Coraz trudniej wyciągnąć stopy z błotnistej mazi. Powietrze staje się coraz\
                \nwilgotniejsze. Korytarz stopniowo się rozszerza, aż w końcu wychodzisz na brzeg\
                \npodziemnego jeziora. Brzegi zarośnięte są roślinnością o grubych, szerokich\
                \nliściach. Sklepienie zawieszone jest wysoko. W kilku miejscach przesączają się\
                \nnie cienkie strugi światła. Rozglądasz się uważnie. Czy to ślepy zaułek?\
                \nNie dostrzegasz innego wyjścia niż to, którym przyszedłeś.",

                 "179": "",

                 "180": f"Ponownie przeszukujesz pokój. W torbie {entities.entity_116.name},\
                \nktórej nie zdążyłeś przejrzeć, znajdujesz klucz. Jest na nim wygrawerowana liczba 45.\
                \nMożesz go wziąść ze sobą.",

                 "181": "Ciskasz w potwora pękiem kluczy, który znalazłeś w jednej z odwiedzonych\
                \nkomnat. Rzut jest celny, ale niegroźny. WILKOŁAK przechwytuje pęk i ucieka.\
                \nRuszasz w pogoń. WILKOŁAK wpada do wąskiej, ale głębokiej rozpadliny znajdującej\
                \nsię w rogu pieczary. Spada na dno i ginie. Przyświecasz sobie latarnią.\
                \nWidzisz w głębi zwaliste cielsko potwora, a obok niego pobłyskują klucze.",

                 "182": "Czy chcesz szukać jakichś sekretnych przejść?",

                 "183": "",

                 "184": "Wycierasz zakrwawiony miecz o skóry leżące pod twoimi nogami.\
                \nNacierasz",

                 "185": "Wchodzisz do wąskiego korytarzyka. Prowadzi on do dużego pomieszczenia",

                 "186": "Udało ci się dotrzeć na drugi brzeg. Masz trzy wyjścia:\
                \njedno prowadzi na zachód (A), a dwa na północ,\
                \njedno z nich jest położone bardziej na zachód (B) niż drugie (C).\
                \nKtóre wybierasz?",

                 "187": "",

                 "188": "",

                 "189": "",

                 "190": "Możesz wybrać dowolny miecz.",

                 "191": "",

                 "192": "'A może by tak wycisnąć coś z tego pajaca?' - myślisz. Sięgasz po miecz. Ech, po co po miecz?\
                \nWystarczy zdzielić go pięścią. Podchodzisz do stwora i zamierzasz się. Istota znika.\
                \nNa dodatek z hukiem opada krata w przejściu, którym dostałeś się do tego pokoju. Rozglądasz się.\
                \nNie widzisz żadnego innego wyjścia. Podchodzisz do fontanny. Istotnie na jej dnie widzisz\
                \nróżne zagadkowe przedmioty: kość potwora, słój z wszystkożerami (wiecznie głodnymi skorupiakami), blaszanego motyla,\
                \nwłócznię i błyszczący kluczyk. To co: chcesz wodę, czy którąś z tych rzeczy. Pamiętaj, ze możesz wziąć tylko jedna rzecz.",

                 "193": "",

                 "194": "",

                 "195": "",

                 "196": "",

                 "197": "",

                 "198": "",

                 "199": "",

                 "200": "Po pewnym czasie dostrzegasz drzwi w południowej ścianie.",

                 "201": "",

                 "202": "",

                 "203": "",

                 "204": "",

                 "205": "",

                 "206": "",

                 "207": "",

                 "208": "",

                 "209": "",

                 "210": "",

                 "211": "",

                 "212": "Dochodzisz do sporego placyku, którego drogi rozchodzą się w czterech kierunkach.\
                \nKtóry wybierasz?",

                 "213": "",

                 "214": "",

                 "215": "",

                 "216": "",

                 "217": "",

                 "218": "",

                 "219": "",

                 "220":
                     "Jeśli wybrałeś kość potwora, słój z wszystkożerami, blaszanego motyla lub włócznię - patrz 109, a jeśli klucz. patrz 366.",

                 "221":
                     "Dochodzisz do skrzyżowania, którym możesz przedostać się na: północ - patrz 339, - wschód - patrz 41, o południe - patrz 173.",

                 "222": "",

                 "223": "",

                 "224": "Po kilkunastu krokach korytarz skręca na wschód. Idziesz dalej.\
                \nW połódniowej ścianie korytarza dostrzegasz drzwi.",

                 "225": "",

                 "226": "Walka trwa dalej. Po drugiej rundzie znów możesz Uciec.\
                \nNa pewno chcesz walczyć dalej?",

                 "227": "",

                 "228": "Korytarz biegnie na północ i skręca w na wschód. Przed sobą widzisz skrzyżowanie.",

                 "229": "",

                 "230": "",

                 "231": "",

                 "232": "",

                 "233": "",

                 "234": "Kończysz walkę z DEMONEM. Czy chcesz zajrzeć do kamiennej puszki stojącej na ołtarzyku?",

                 "235": "",

                 "236": "",

                 "237": "",

                 "238a": "Napotykasz grupę wędrujących Potworów. Są to: GREMLIN, LICHA, BRONGO, ORKONIK i SAMASKÓRA.\
                \nPo walce z każdym możesz ratować się Ucieczką.",

                 "238b": "",

                 "239": "",

                 "240": "",

                 "241": "Pamiętaj, że możesz nabrać wody z jeziora - patrz:",

                 "242": "",

                 "243": "",

                 "244": "",

                 "245": "",

                 "246": "",

                 "247": "",

                 "248": "",

                 "249": "",

                 "250": "",

                 "251": "Wychodzisz tędy, którędy wszedłeś.",

                 "252": "",

                 "253": "",

                 "254": "",

                 "255": "",

                 "256": "",

                 "257": "",

                 "258": "",

                 "259": "",

                 "260": "",

                 "261": "",

                 "262": "",

                 "263": "",

                 "264": f"Trudno przejść przez to zwalisko kamieni.\
                \nNa szczęście korytarz nie wije się we wszystkie strony,\
                \nlecz prowadzi prosto na północ.",

                 "265": "",

                 "266": "",

                 "267": "",

                 "268": "Krótki tunel dochodzi do zbutwiałych, starych drzwi.",

                 "269": "Wyciągasz z plecaka linę. Jest ognioodporna i zakończona hakiem.\
                \nPodchodzisz do krawędzi. Szerokim zamachem rzucasz hak między skały na przeciwnym brzegu.\
                \nZaczepił się. Przywiązujesz drugi koniec liny. Będziesz 'szedł' wisząc na rękach.\
                \nOpuszczasz się. Nagle... trach! Hak puścił. Wdrapujesz się z powrotem.",

                 "270": "",

                 "271a": "Zdejmujesz ze stojaka bogato zdobiony, błyszczący miecz. Obracasz rękojeść w dłoni.\
                \nNagle broń wypada ci z ręki i rani ramie.",

                 "271b": "Wybierasz inny. Wygląda skromnie. Dobrze leży w dłoni.\
                \nOdrzucasz swój stary miecz. Ten z sykiem zamienia się w szczura. Dobry to, czy zły znak?\
                \nChcesz swój nowy miecz wymienić na inny?",

                 "272": "",

                 "273": "",

                 "274": "",

                 "275": "",

                 "276": "",

                 "277": "",

                 "278": "",

                 "279": "",

                 "280": "",

                 "281": "",

                 "282": "",

                 "283": "",

                 "284": "Korytarz jest coraz węższy, Ze sklepienia zwisają długie, kamienne brody.\
                \nMogą lada chwila urwać się",

                 "285": "",

                 "286": "",

                 "287": "",

                 "288": "",

                 "289": "",

                 "290": "",

                 "291": "Kierujesz się do wyjścia, gdy nagle nie wiadomo skąd\
                \ntrafia cię w brzuch mała, błękitna strzałka.",

                 "292": "",

                 "293": "",

                 "294": "",

                 "295": "",

                 "296": "Korytarz biegnie na zachód i skręca na północ.",

                 "297": "",

                 "298": "",

                 "299": "",

                 "300": "",

                 "301": "Możesz spróbować otworzyć drzwi",

                 "302": "",

                 "303": "",

                 "304": "",

                 "305": "W tej komnacie ukryte jest coś bardzo wartościowego. Żeby to znaleźć musisz wybrać jedną z podanych metod:",

                 "306": "Nabierasz wody. Jest zaczarowana. Chowasz naczynie do plecaka. Dostajesz +2s. Patrz - 109",

                 "307": "",

                 "308": "",

                 "309": "",

                 "310": "Tylko dziesięć kroków dzieli Cię od zmurszałych, drewnianych drzwi.",

                 "311": "",

                 "312": "",

                 "313": "",

                 "314": "",

                 "315": "",

                 "316": "Idziesz korytarzem na południe",

                 "317a": "Drzwi ustępują. Bucha spoza nich przerażliwy smród.\
                \nW nikłym swietle oliwnej lampy widzisz porozrzucane na całym pomieszczeniu jakieś szczątki.\
                \nPrzyglądasz sie bliżej. To kości! odwracasz z obrzydzeniem twarz. A czego tu się spodziewałeś?\
                \nWojennych Kwiatów? Tańczących elfów? Melancholijnej muzyki? To są, bracie\
                \npodziemia - królestwo zła. I dlatego ...///...",

                 "317b": f"{entities.entity_317.name} leży u twych stóp. Ciągle jeszcze się brzydzisz?",

                 "318": "",

                 "319": "",

                 "320": "",

                 "321": "",

                 "322": "",

                 "323": "",

                 "324": "",

                 "325": "",

                 "326": "",

                 "327": "",

                 "328": "",

                 "329": "",

                 "330": "Ta komnata ma tylko jedno wyjście: to, którym się tu dostałeś. Wracasz do korytarza.",

                 "331": "Króciutki tunel prowadzi cię do jakiegoś pomieszczenia.",

                 "332a": "Wrota obite są grubą metalową blachą. Ukośnie przebiegają wąskie metalowe\
                \npasy, w miejscach przecięcia nabite żelaznymi guzami. Zapierasz się plecami.\
                \nStopy ślizgają się po grząskim gruncie. Wrota ustępują. Przeraźliwie skrzypią.\
                \nSłyszysz dobiegający z komnaty pospieszny szmer. Wciskasz się do szpary i\
                \nopierając się plecami o skałę z całą mocą odpychasz wrota. Opornie otwierają się\
                \nna całą szerokość. To był szalony wysiłek.",

                 "332b": f"Podnosisz latarnię na wysokość\
                \noczu i... serce podchodzi ci do gardła. Schowany za ścianą stoi {entities.entity_332.name}. Ciało ma\
                \nwygięte w pałąk. Wysoko za głową oburącz trzyma miecz. Wypina do przodu\
                \nowłosiony brzuch. Szalone oczy nabiegły mu krwią. Szczerzy zaciśnięte zęby.\
                \nJeszcze chwila i ogromny miecz przetnie powietrze. Sięgasz po swój miecz. W\
                \nokamgnieniu {entities.entity_332.name} wyprowadza cios. Udaje ci się odskoczyć. To będzie walka na\
                \nśmierć i życie.",

                 "333": "",

                 "334": "",

                 "335": "",

                 "336": "W niewielkiej odległości dostrzegasz jakieś drzwi. Podchodzisz bliżej",

                 "337": "",

                 "338": "",

                 "339": "",

                 "340": "",

                 "341": "",

                 "342": "",

                 "343": "",

                 "344": f"Ognista kula jest znakomitą bronią przeciw STRAŻNIKOWI TAJEMNICY.\
                \nJest bardzo skuteczna i szybka. Wraca do twojej ręki po każdym rzucie.\
                \nDaje ci to następujące korzyści podczas walki:\
                \n*możesz dodać 2 do liczby uzyskanej na kostkach przy określaniu siły ataku,\
                \n*każdy atak powoduje nie 2 lecz 3 rany, *gdy STRAŻNIK zrani cię, rzuć kostką:\
                \njeśli uzyskasz liczbę nieparzystą, zadaje ci - jak normalnie - 2 rany;\
                \njeśli wyrzucisz 2 lub 4 otrzymujesz 1 ranę; jeśli masz 6, nie trafia cię w ogóle.",

                 "345": "Idziesz w stronę skrzyżowania. Możesz pójść na:",

                 "346": "",

                 "347": "",

                 "348": "",

                 "349": "Delikatnie wsuwasz stopę w wąską szparę. Biodrami rozpychasz drzwi.\
                \nOdskakują na bok. To jest metoda! Wyczuwasz lekki zapach suszonych ziół.\
                \nPrzy lewej ścianie stoją dwie gładkie kolumienki.\
                \nMiedzy nimi na wysokości oczu rozciągnięta jest granitowa półka.\
                \nStoją tam dwie lampki, a na środku kamienne pudełko.\
                \n\
                \nPosadzka wyłożona jest włochatymi skórami zwierząt i potworów.\
                \nTo chyba podziemna kaplica! Pod ścianą, naprzeciw ołtarzyka widzisz niski, wykuty w skale stół.\
                \nCos tam na nim stoi. Podnosisz wyżej latarnię. Och, królu Almanhagorze, to dwie wazy pełne złota.\
                \nKażda ma taki sam wyszukany kształt. Z jednej strony ozdobiona jest łbem jakiegoś stwora,\
                \nz drugiej - przymocowane są dwa połyskujące skrzydła. Czy chcesz zabrać złoto?",

                 "350": "",

                 "351": "Przeciskasz się przez zawalony kamieniami korytarz.",

                 "352": "",

                 "353": "",

                 "354": "",

                 "355": "",

                 "356": "",

                 "357": "",

                 "358": "Zaczepiłeś linę i już 'idziesz' po niej. Wtem z wnętrza rozpadliny bucha\
                \njęzor ognia. Jeśli masz przy sobie napój niewidzialności - wypij go.\
                \nOgień nieczyni ci krzywdy. Ale napój przestaje działać zanim docierasz do drugiego brzegu.",

                 "359": "",

                 "360": "",

                 "361": "",

                 "362": "",

                 "363": "",

                 "364": f"Popychasz drzwi, uchylają się. Otwiera się ciemna czeluść.\
                \nWchodzisz oświetlając drogę latarnią. Pod stopami czujesz kamyki.\
                \nZ przeciwległego końca pokoju dochodzi ciebie ciche chrapanie.\
                \nNa podłodze śpi {entities.entity_116.name}. Obok niego leży jakieś pudełko.",

                 "365": "",

                 "366": "",

                 "367": "",

                 "368": "",

                 "369": "",

                 "370": "",

                 "371": "",

                 "372": "",

                 "373": "",

                 "374": "To nie korytarz, raczej jakiś kanał. Nogi zapadają się w błotnistą maź.\
                \nTunel zmienia kierunek: najpierw skręca na południe, później na wschód, a w końcu na północ.",

                 "375": "",

                 "376": "",

                 "377": "",

                 "378": "",

                 "379": "",

                 "380": "",

                 "381": "",

                 "382":
                     "Po pewnvm czasie korytarz skręca na północ. Na zakręcie mozesz zjeść Prowiant. Patrz - 134",

                 "383": "Ogarnia cię wściekłość. Chwytasz za miecz i atakujesz - patrz 318.",

                 "384":
                     "Pięćdziesiąt kroków naprzód, a potem skręt W lewo (czyli na północ) i trzydzieści kroków. Patrz 221.",

                 "385": "Możesz wydostać się z komnaty DEMONÓW albo przez wschodnie albo przez zachodnie drzwi.",

                 "386":
                     "Zbliżasz sie do skrzyżwania. Możesz iść albo na zachÓd - patrz 345, albo na wschÓd - patrz 273.",

                 "387": "Wkładasz klucze do zamka. Najpierw pierwszy... stuk, później drugi... stuk i trzeci... stuk. Detikatnie podnosisz wieko skrzvni.\
                \nNa jej dnie leżą jakieś papiery. Nie, to złożony na 16 stron, ilustrowany druk. ostrożnie przewracasz kartki. Znajdujesz w nim dokładny opis wędrówki po podziemnym labiryncie. Zatrzymaj go, bo to papier niezwykle wartościowv"
                 },
            'es':
                {"xxx": ""},
            'fr':
                {"xxx": "",
                 "00a": "\rEn vous promenant dans les souterrains, vous trouverez différents types d'armes et d'objets. \
                 \nSouvenez-vous que - à l'exception de l'épée - chaque arme ne peut être utilisée qu'une seule fois. \
                 \nDe même, les objets trouvés sont à usage unique. \
                 \nVous pouvez emporter une bouteille d'élixir avec vous.",
                 "00b": "Hé, Brave ! \
                 \n\
                 \nOn dit de vous que de l'eau glacée coule dans vos veines au lieu de sang, \
                 \net que vos muscles sont faits de l'acier le plus noble ? \
                 \nSi c'est le cas, regardez vers le soleil couchant. \
                 \nLà-bas, aux frontières du royaume d'Almanhagor, commence le souterrain inexploré. \
                 \nVous seul pouvez dévoiler son Grand Secret. Avancez !",
                 "01": "L'entrée du souterrain est large, envahie par l'herbe et les buissons luxuriants. \
                 \nVous ajustez vos vêtements et votre équipement. \
                 \nAllumez votre lanterne ! Vous entrez dans le corridor. Il est haut, et vous n'avez pas besoin de vous baisser. \
                 \nIl mène droit vers le nord. Bientôt, vous arrivez à un carrefour. \
                 \nIl a la forme de la lettre T. Les branches mènent à l'ouest, à l'est et au sud (d'où vous venez)."
                 },
            'it':
                {"xxx": ""},
            'cn':
                {"xxx": ""},
            'jp':
                {"xxx": ""},
        }
        constants.translation = translation
        if translation in gameboook:
            return gameboook[translation], constants.translation
        else:
            functions.debug_message('not available, language set to english')
            return gameboook['en']  # english by default
