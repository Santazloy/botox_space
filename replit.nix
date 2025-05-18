{ pkgs }: {
  deps = [
    pkgs.python312Full     # или pkgs.python3
    pkgs.ffmpeg            # <- подключаем ffmpeg
    pkgs.postgresql        # если нужен клиент Postgres
    pkgs.cacert            # SSL сертификаты
  ];
}