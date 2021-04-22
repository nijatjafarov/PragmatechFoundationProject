1. Translator ve assebler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
    - Translator əsasən yüksək səviyəli dildə yazılmış source code-u aşağı səviyə olan machine code-a çevirən bir alətdir. Bu baxımdan Compiler, interpreter və Assembler kimi çeviricilərə ümumi olaraq Translator deyilir. Assembler isə aşağı səviyyə Assembly dilində yazılmış kodu maşın dilinə çevirən çeviricidir.
2. Rəqəm və ədədlərin maşın dilinə tərcümə olunma prosesini bilirik. Bəs hərflər və simvollar necə tərcümə olunur?
    - Hərflər və simvollar maşın dilinə bəlirlənmiş standartlar əsasında çevrilirlər. Bu standartlara verilə biləcək örnəklər ASCİİ və Unicode-dur. ASCİİ(American Standard Code for Information Interchange) açılışı "İnformasiya mübadiləsi üçün amerikan standart kodu"-dur. Əsasında ingilis əlifbası üçün yazılmış standartdır və 256 simvolu əhatə edir. Lakin, dünyada fərqli dillər və simvollar olduğu üçün ASCİİ qlobal informasiya mübadiləsi üçün kifayət etmir və nəticədə Unicode yaradılıb. Unicode-da simvollar üçün 1 112 064 yer ayrılıb və indiyə qədər bu yerlərin 100 000-dən çoxu istifadə olunub.
3. Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri hansılardır və qısaca izahatlarını yazın
    - Əksər proqramlaşdırma dillərində istifadə olunan təməl data növlərinə aşağıdakıları nümuna göstərmək olar:
        - Integer
        - Floating-point number
        - Character
        - String
        - Boolean

        **Integer**: proqramlaşdırma zamanı tam ədədlərin yazılması məqsədi ilə istifadə olunur və bu baxımdan fundamental data növü hesab edilə bilər.
        **Floating-point number**: həqiqi ədədlərin istifadə olunması üçün lazımdır.
        **Character**: hərf, rəqəm, simvolların ASCİİ və ya Unicode-da olan encoding qarşılığından istifadə etmək məqsədilə işlədilir.
        **String**: mətn formasında olan datalardan istifadə üçün mövcuddur.
        **Boolean**: mümkün iki qiymətdən birini alan data tipi. Doğru və ya yalnış kimi məntiqi nəticələr əldə etmək üçün istifadə olunur.
4. Type Conversion ya da Type Casting nədir? Hansı hallarda ehtiyac duyulur
    - Type Conversion və ya Type Casting bir data tipinin digər data tipinə çevrilməsidir. Uyğun olaraq bir data tipinin digər data tipinə çevrilməsi lazım gəldiyi zaman istifadə edilir. Kiçik bir nümunə: Marketdən bir neçə məhsul alınır və onların hər birinin qiyməti rasional ədəd olaraq manat və qəpik olaraq birlikdə göstərilir(Məs: 3.45 manat), amma bizə bütün məhsulların ümumi qiymətini topladığımız zaman tutarı sadəcə tam ədədlə (Məs: 23 manat) ifadə etmək lazım gələ bilər. Bu zaman float tiplərin cəmini integer tipinə convert etmək lazım gəlir.
5. Operator precedence nədir və əhəmiyyətini izah edin
    - Operator precedence operatorların yerinə yetirilmə öncüllüyünü bildirir. Bütün operatorlar bərabər səviyəli olmurlar və onlar arasında iyerarxiya mövcud olur. Məsələn, qüvvətə yüksəltmə operatoru vurma operatorundan və o da toplama operatorundan daha güclüdür, bu baxımdan sözügedən 3 operatorun birlikdə işləndiyi statement olduğu zaman ilk öncə qüvvətə yüksəltmə, daha sonra vurma və daha sonra toplama operatorları yerinə yetiriləcək.
6. Automatic Type Conversion ve Type Conversion Methodlar arasındakı fərqləri izah edin.
    - Bu barədə araşdırdığım zaman ətraflı məlumat əldə edə bilmədim. Çıxardığım nəticə bu oldu ki, məncə Automatic Type Conversion-la proqramlaşdırma dillərinin sahib olduğu built-in method olaraq Type Conversion Methodlar eyni və ya bənzərdir. Hər ikisi zəif data tipini güclü data tipinə çevirirlər yanlış anlamamışamsa, amma fərq olmasa dilə əlavə olaraq belə built-in methodlar niyə qoyulsunki? Təəssüf ki, bu fərqləri göstərəcək bir mənbə tapmağım mümkün olmadı.
7. Implicit ve Explicit type conversiton nədir?
    - Implicit çevirmə zəif data tipini güclü data tipinə çevirir:
    `char` -> `int` -> `long` -> `float` -> `double`
    Implicit Type Conversion(Automatic) tip çevirmənin compiler tərəfindən yerinə yetirildiyi çevirmədir, digər tip çevirmə olan Explicit Type Conversion(Manual) isə çevirmənin developer tərəfindən edildiyi çevrilmədir. Burada isə əksinə olaraq güclü data tip zəif data tipə çevrilir:
    `double` -> `float` -> `long` -> `int` -> `char` Məsələn:


    ```c
    double da = 3.3;
    double db = 3.3;
    double dc = 3.4;
    int explicit_result = (int)da + (int)db + (int)dc; // result == 9
    int implicit_result = da + db + dc; // result == 10
    // Explicit çevirmə ilə nəticə 9 alındığı halda, Implicit çevirmə ilə nəticə 10 olur.
    ```

    Nümunədən göründüyü kimi Implicit çevirmədə bir dəyər digərinə olduğu kimi mənimsədilir. Explicit çevirmədə isə mənimsədilən dəyərin qarşısına çevrilmək istədiyi data tipi bildirilir. Implicit çevrilmənin dezavantajı çevirməni compiler apardığı üçün bəzən gözlənilən nəticənin alınmaması ola bilər, digərində isə developer birbaşa özü müdaxilə edir. Bundan başqa bəzi data tipləri vardır ki, bunlar çevrilməyə uyğun deyillər (Məs: boolean və char) və ya  bu zaman Explicit çevrilmə zamanı xəta baş verir. Bundan başqa böyük data tipi kiçik data tipə çevirən zaman (Məs: float -> integer) datada itki baş verə bilər (Məs: 7.23 -> 7).
8. List,Tuple,Dict data növləri arasındakı oxşar və fərqli cəhətlər nələrdir?
    - List, Tuple və Dict, üçünün oxşar cəhəti içlərinə bir neçə data yerləşdirməyin mümkünlüyüdür. Dict-in digər ikisindən fərqi unordered data, digərlərinin isə ordered data tipi olmasıdır. List və Tuple-dan fərqli olaraq Dict-də index hər hansı bir məna daşımır. Burada key-value prinsipindən istifadə olunur. Tuple-ın List və Dict-dən fərqi immutable olmasıdır. Buna görə də Tuple-a data əlavə edib çıxarmaq, həmçinin dəyişdirmək olmaz. Digərləri üçün isə bu hal keçərli deyil. List-in Dictdən fərqi ordered data tipi olması, Tuple-dan fərqi isə mutable olmasıdır. Yəni List-də elementlərin yerləşdiyi index məna daşıyır və List data əlavə edib çıxarmağa, həmçinin dəyişməyə imkan verir.
