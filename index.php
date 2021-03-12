<?
    $connection = new PDO('mysql:host=localhost; dbname=amster; charset=utf8', 'root', '');
    $data = $connection->query("SELECT * FROM products");

?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Amster</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <script src="js/main.js" defer></script>
</head>

<body>
    <section class="banner"></section>
    <div class="products">
        <div class="wrapper">
            <div class="products__content">
                <?
                    foreach ($data as $item) {
                        echo "
                            <div class=\"product\">
                                <a class=\"product__link\" href=\"#\">
                                    <img src=\"img/" . $item['id_product'] . ".jpg\" alt=\"\" class=\"product__image\">
                                </a>
                                <a class=\"product__link\" href=\"#\">
                                    <p class=\"product__name\">" . $item['name'] . "</p>
                                </a>
                                    <p class=\"product__price\">" . $item['price'] . " ₽</p>
                                    <button class=\"product__buy\" 
                                    data-id=\"" . $item['id_product'] . "\">Купить</button>
                            </div>";
                    }
                ?>
            </div>
        </div>
    </div>
    <?
    if (isset($_POST['id_product'])){
        $idProduct = $_POST['id_product'];
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $phone = $_POST['phone'];
        $obtaining = $_POST['obtaining'];
        $query = "
                INSERT INTO orders (
                    id_product, name, surname, phone, obtaining
                ) VALUES ("
                . $idProduct . ", '"
                . $name . "', '"
                . $surname . "', '"
                . $phone . "', "
                . $obtaining . "
                )";
        $connection->query($query);
    }
    ?>
    <div class="modal-window">
        <form method="POST" class="form">
            <input type="text" name="id_product" style="display: none">
            <input type="text" class="form__input" name="name" placeholder="Имя"></input>
            <input type="text" class="form__input" name="surname" placeholder="Фамилия"></input>
            <input type="text" class="form__input" name="phone" placeholder="Номер телефона"></input>
            <select class="form__input" name="obtaining">
                <option value="0">Самовывоз</option>
                <option value="1">Доставка</option>
            </select>
            <button class="form__button">Оформить заказ</button>
        </form>
        <div class="modal-window__close"></div>

    </div>
</body>

</html>