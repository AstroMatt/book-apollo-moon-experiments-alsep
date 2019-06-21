.. _Lunar Surface Magnetometer:

********************************
Lunar Surface Magnetometer (LSM)
********************************


.. csv-table:: Lunar Surface Magnetometer (LSM)
    :stub-columns: 1

    "Ośrodek badawczy", "University of Arizona, USA"
    "Misje", "Apollo 12, 15, 16"
    "Nazwa eksperymentu (j. ang.)", "Lunar Surface Magnetometer"
    "Nazwa eksperymentu (j. pol.)", "Magnetometryczny pomiar powierzchni Księżyca"
    "Dziedzina", "Magnetometria"


Przedmiot badania
=================
Pole magnetyczne Ziemi i Księżyca składa się z dwóch elementów składowych: jednej zmieniającej się w czasie oraz drugiej stabilnej. Część niestabilna jest wynikiem przejścia fal elektromagnetycznych. Część stabilna pola magnetycznego Ziemi (która wchodzi w interakcję z kompasem) przyjmuje wartości od 35 000 nT na równiku do 60 000 nT na biegunach. Wartość gamma pola magnetycznego Księżyca wynosi 6 do 100 nT. Jest to spowodowane obecnością naturalnie występującego zjawiska magnetyzmu w skałach księżycowych. Minerały te powstały na wczesnym etapie ewolucji Księżyca, gdy pole magnetyczne było znacznie silniejsze :cite:`Calio1970`, :cite:`Allen1972`, :cite:`Brett1972`.

Obecnie uznawana teoria wyjaśnia przyczynę naturalnego powstawania zjawiska magnetyzmu skał. Gdy meteoryt znacznej wielkości uderzy w powierzchnię Księżyca w skutek impaktu i wysokich temperatur następuje wyparowanie materiału skalnego, jak również wyrzut w kosmos części powierzchni. Obiekty powstałe w skutek tego działania formują chmury odłamków gruzu i gazów. Chmury te są większe niż Księżyc. W wyniku uwolnienia znacznej ilości ciepła podczas zderzenia, większość gazu zamienia się w zjonizowaną plazmę, w której atomy są pozbawione jednego lub więcej elektronów. Taka plazma pozbawiona jest własności magnetycznych. Chmura rozprzestrzeniając się wokół Księżyca spycha frontalnie własne pole magnetyczne Księżyca. Do przemieszczenia plazmy wokół Księżyca dochodzi w ciągu około 5 minut. W skutek czego zepchnięte pole magnetyczne stanie się znaczne. W tym czasie odłamki skalne opadną na powierzchnię Księżyca koncentrując się na krańcach antypodalnych. W przypadku gdy formacje skalne opadną w trakcie wpływu wysokiego pola magnetycznego, mogą przejść proces nagłej magnetyzacji (ang. *shock magnetization*). Dla porównania, gdy skała zostaje poddana uderzeniu przez młot, może nagle stracić własności magnetyczne i przyjąć te z otaczającego regionu :cite:`Jones1995`, :cite:`Apollo12PressKit`.

Elektryczne własności materiału tworzącego Księżyc determinują jego pole magnetyczne. W wypadku gdyby Księżyc był doskonałym izolatorem fala elektromagnetyczna wiatru słonecznego przeszła by przez niego niezakłócona i połączyła linie pola wokół Księżyca. W skutek czego przepływający prąd wytworzy pole magnetyczne. Pole to niesione z wiatrem słonecznym przyczynia się do powstania systemu prądów elektrycznych na Księżycu i jego powierzchni. Prady te, mogą tworzyć pole magnetyczne, próbujące przeciwdziałać polu jonowemu wiatru słonecznego. Przyczyniłoby się to do zmiany łącznego pola magnetycznego zmierzonego na powierzchni Księżyca. Gdyby zaś istniały struktury geologiczne zachowujące się jak przewodnik, prąd elektryczny przepłynąłby przez niego :cite:`Apollo12PressKit`, :cite:`Brett1972`.

Celem badawczym eksperymentu był pomiar pola magnetycznego powierzchni Księżyca oraz ustalenie jak naładowane cząsteczki wiatru słonecznego wchodzą w interakcję z polem magnetycznym. Część cząstek jest wchłaniana przez warstwy powierzchniowe Księżyca, a pozostała część może zostać odbita lub przeniesiona na drugą jego stronę.

Pomiaru dokonano niezależnie za pomocą równoległego zbadania różnic wartości potencjału elektrycznego wiatru słonecznego przy powierzchni jak również niezakłóconego odczytu w trakcie sondowania z orbity. W tym celu wykorzystano misję robotyczną Explorer 35 orbitującą wokół Księżyca.


Materiały i metody
==================
.. figure:: img/alsep-LSM-diagram.png
    :name: figure-alsep-LSM-diagram

    Diagram przedstawia eksperyment Lunar Surface Magnetometer (LSM). Źródło: :cite:`Apollo12PressKit`.

Parametry techniczne :cite:`Jones1995`, :cite:`Apollo12PressKit`:

    * Wielkość po rozłożeniu: 101,6 cm wysokości, z 152,4 cm odległości od głowicy
    * Masa: 7,94 kg
    * Szczytowy pobór mocy:

        * Tryb rozpoznania lokacji: 11,5 W
        * Tryb naukowy w dzień: 6,2 W
        * Tryb naukowy w nocy: 12,3 W
        * Tryb kalibracji: 10,8 W

Magnetometr pozwalał na pracę w trzech trybach :cite:`Calio1970`:

    #. Tryb rozpoznania lokacji (ang. *Site Survey Mode*) - Stan początkowy przed przejściem do każdego pozostałego trybu. Stworzony w celu lokalizacji oraz identyfikacji wpływu magnetycznego obecnego na miejscu pomiaru. Zastosowany w celu likwidacji jego wpływu przy późniejszej interpretacji danych.

    #. Tryb naukowy (ang. *Scientific Mode*) - Normalny tryb operacyjny, w który wartość pola magnetycznego oraz jego skierowanie jest stale rejestrowane. Trzy sensory magnetyczne dostarczają sygnał proporcjonalny do występowania składowych równoległych odpowiednio do ich osi. Każdy czujnik próbkuje z częstotliwością 3 Hz. Jest to wartość większą niż częstotliwość zmian pola magnetycznego. Wszystkie sensory rejestrowały zmiany z rozdzielczością 0,2 nT (nano Tesli)  w trzech zakresach:

        * -100 do +100 nT,
        * -200 do +200 nT,
        * -400 do +400 nT.

    #. Tryb kalibracyjny (ang. *Calibration Mode*) - Włączany automatycznie w 12 godzinnych interwałach w celu precyzyjnego ustawienie czujników magnetometru i poprawy dryftu od wartości referencyjnych ustawionych laboratoryjnie.

Za projekt trójosiowego magnetometru transduktorowego (ang. *tri-axis fluxgate magnetometer*), jak również za późniejszą analizę danych odpowiadali Dr Charles P. Sonett (NASA/Ames Research Center), Dr Jerry Modisette (NASA/Manned Spacecraft Center) i Dr Palmer Dyal (NASA/Ames Research Center).

Przebieg eksperymentu
=====================
Podczas misji :ref:`Apollo 15` w 1971 roku i później podczas :ref:`Apollo 16` w 1972 roku na orbicie Księżyca umieszczono wykrywacz elektronowy. Urządzenie wykorzystano do wykonania zdalnego mapowania pola magnetycznego powierzchni. Pomiar ten pozwolił na pokrycie 10% powierzchni Księżyca i umożliwił dostrzeżenie korelacji między kraterami meteorytowymi (ang. *meteor impact basins*) - ciemniejsze struktury, o najczęściej kolistym kształcie na stronie Księżyca zorientowanej do Ziemi, od silnego pola magnetycznego po przeciwnej stronie (niewidocznej z Ziemi).

W wyniku pomiarów pola magnetycznego za pomocą orbitujących satelit określono średnią wartość równą 8 nT. Za pomocą magnetometru dokonano również pomiaru wariacji w czasie spowodowanej propagacją fali elektromagnetycznej w wyniku :term:`SPE`.

W trakcie eksperymentu :ref:`Lunar Surface Magnetometer` za pomocą trójosiowego magnetometru transduktorowego (ang. *tri-axis fluxgate magnetometer*) zmierzono zmiany pola magnetycznego Księżyca w czasie. Ze względu na możliwość zmiany amplitudy, częstotliwości oraz kierunku pola magnetycznego Księżyca sensor dokonywał pomiarów w trzech wymiarach za pomocą czujników umieszczonych na niewielkich, ustawionych ortogonalnie wysięgnikach zrobionych z włókna szklanego. Części wysuwały się ze :ref:`stacji centralnej <Central Station>`.

Układ elektroniczny mieścił się w osłonie u podstawy trzech wysięgników. W tym miejscu zlokalizowano również żyroskop elektromechaniczny. Urządzenie to pozwalało na ustawienie w trybie kalibracji sensorów w dowolnym kierunku. Astronauta ustawiając magnetometr w przedziale +3° w kierunku wschód-zachód używał wskaźnika cienia (ang. *shadwograph*) na centralnej strukturze. Konieczne było przestrzeganie wewnętrznego marginesu +3° w osi pionowej. W tym celu użyto poziomicy zamontowanej na ramieniu wysięgnika sensorów.


Rezultaty
=========
Eksperyment :ref:`Lunar Surface Magnetometer` został użyty do zbadania zmiany wartości pola magnetycznego na powierzchni Księżyca, jak również do określenia własności elektrycznych Księżyca. Przyczynił się również do lepszego zrozumienia wewnętrznej temperatury i poznania pochodzenia oraz historii tego ciała niebieskiego.

Księżyc w przeciwieństwie do Ziemi nie posiada pola magnetycznego. Jest to spowodowane brakiem wewnętrznego procesu wywołującego efekt dynamo. Okazało się zaskoczeniem, gdy magnetometr ustawiony przez astronautów wykrył nikłe pole magnetyczne. Eksperyment :term:`LSM` udokumentował stałą wartość na poziomie 38 nT dla miejsca lądowania :ref:`Apollo 12` i 6 nT dla :ref:`Apollo 15` :cite:`Calio1970`, :cite:`Allen1972`.

Uważa się, że magnetyzm powierzchni Księżyca jest pozostałością z czasu, gdy jego pole magnetyczne było aktywnie tworzone przez jądro. Pozostały efekt magnetyczny może być również spowodowany zderzeniem lub zderzeniami w przeszłości z innymi ciałami niebieskimi tj. asteroidy czy komety, które mogły przyczynić się do nadania niewielkich własności magnetycznych. Ta szczątkowa własność magnetyczna jest w fazie zaniku  :cite:`Calio1970`, :cite:`Allen1972`, :cite:`Brett1972`.

