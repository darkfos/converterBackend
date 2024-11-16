from typing import Dict, Union

# Local
from src.api.auth import AuthService
from src.api.dep import UOW
from src.api.core.schemas import AllHistoriesSchema, BaseHistorySchema
from src.api.enums_sett import AuthEnum

auth: AuthService = AuthService()


class HistoryService:


    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def create_history(
            new_history: BaseHistorySchema,
            uow: UOW,
            token: str = "",
            token_data: Dict[str, Union[str, int]] = {}
    ) -> bool:
        async with uow as connection:

            # Set data
            connection.history_rep.model.id_user = token_data.get("sub")
            connection.history_rep.model.name_operation = new_history.name_operation
            connection.history_rep.model.date_operation = new_history.date_operation

            res = await connection.history_rep.add_one()
            print(res)
            return res


    @auth(type_token=AuthEnum.DECODE.value)
    @staticmethod
    async def get_all_histories_for_user(
            uow: UOW,
            token: str = "",
            token_data: Dict[str, Union[str, int]] = {}
    ) -> AllHistoriesSchema:
        async with uow as connection:
            res = await connection.history_rep.get_all_by_us_id(id_user=token_data.get("sub"))
            all_histories: AllHistoriesSchema = AllHistoriesSchema(histories=[])
            for history in res:
                all_histories.histories.append(
                    BaseHistorySchema(
                        name_operation=history.get("name_operation"),
                        date_operation=history.get("date_operation")
                    )
                )
            return all_histories