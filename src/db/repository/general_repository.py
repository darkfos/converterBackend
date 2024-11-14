from typing import Any, List, Union


class GeneralRepository:
    def __init__(self, model) -> None:
        self.model: Any = model

    async def add_one(self, values: tuple) -> bool:
        pass

    async def get_all(self) -> List:
        pass

    async def get_by_id(self, id_m: int) -> Union[None, Any]:
        pass

    async def update_by_id(self, id_m: int) -> bool:
        pass

    async def del_by_id(self, id_m: int) -> bool:
        pass