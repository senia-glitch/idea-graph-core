# Ядро графа идеи

Библиотека без интерфейса и без моделей: карточки, связи, операции, журнал изменений, отмена.

```python
from idea_graph_core import Store, HUMAN, views

store = Store.create("папка-проекта", "Запись к врачу")       # пустой граф: корневой карточки нет
store.apply([{"op": "add_card", "kind": "домен", "title": "Пациенты частных клиник"}], HUMAN)
store.apply([{"op": "add_card", "kind": "сценарий", "title": "Утром нужно записаться", "parent": "c1"}], HUMAN)
print(views.outline(store))            # оглавление графа — так его читает агент
print(views.changes_text(store, 1))    # что изменилось после ревизии 1
store.undo(store.revision)             # отмена ревизии новой ревизией
```

Правила, которые проверяет ядро: связи ведут к существующим карточкам, идентификаторы
не повторяются, правка человека главнее правки агента (`base_revision` в `apply`).
## Банки

Общие хранилища записей проекта, которые пишет один этап и читают другие (например, конкуренты):

```python
bank = store.bank("competitors")
bank.put("competitor", {"name": "Докдок", "url": "https://dokdok.example"}, "package:recon",
         sources=["https://dokdok.example"], key="dokdok.example")   # тот же key — обновление, не дубль
bank.list("competitor")
```

Запись: `{id, type, key, data, sources, schema_version, author, created, updated}`; структуру `data` определяет
пакет-автор. Файлы: `<проект>/.idea-graph/banks/<имя>.json`; граф и его ревизии банки не затрагивают.

Файлы графа лежат в `<папка проекта>/.idea-graph`: `graph.json`, `journal.jsonl`, `layout.json`.

## Установка

```
pip install -e .
```


## Тесты

```
pip install pytest
python -m pytest
```
