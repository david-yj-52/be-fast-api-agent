from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.config.sqlite_session import Base
from app.constant.table_name import AgentTableName
from app.dao.cmn.default_model_mixin import DefaultModelMixin


class AhLclMpmsProdInf(Base, DefaultModelMixin):
    __tablename__ = AgentTableName.AH_LCL_MPMS_PROD_INF.value

    ref_obj_id: Mapped[str] = mapped_column(String(100), nullable=False)
    pltf_id: Mapped[str] = mapped_column(String(100), nullable=False)
    prod_id: Mapped[str] = mapped_column(String(100), nullable=False)
    prod_nm: Mapped[str] = mapped_column(String(40))
    prod_base_url: Mapped[str] = mapped_column(nullable=False)
    tgt_ele_nm: Mapped[str] = mapped_column(String(100), nullable=False)
    tgt_ele_typ: Mapped[str] = mapped_column(String(40), nullable=False)
    tgt_ele_val: Mapped[str] = mapped_column(nullable=False)


class AnLclMpmsProdInf(Base, DefaultModelMixin):
    __tablename__ = AgentTableName.AN_LCL_MPMS_PROD_INF.value

    pltf_id: Mapped[str] = mapped_column(String(100), nullable=False)
    prod_id: Mapped[str] = mapped_column(String(100), nullable=False)
    prod_nm: Mapped[str] = mapped_column(String(40))
    prod_base_url: Mapped[str] = mapped_column(nullable=False)
    tgt_ele_nm: Mapped[str] = mapped_column(String(100), nullable=False)
    tgt_ele_typ: Mapped[str] = mapped_column(String(40), nullable=False)
    tgt_ele_val: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        Index(
            "UK_"+ AgentTableName.AN_LCL_MPMS_PROD_INF.value + "_01",
            "pltf_id",
            "prod_id",
            "tgt_ele_typ",
        ),
    )
    
    def to_history(self) -> AhLclMpmsProdInf:
        """Kotlin의 toHistory()와 동일한 역할"""
        # 1. 현재 객체의 필드들을 dict로 추출 (SQLAlchemy 내부 상태 필드 제외)
        excluded_fields = {'_sa_instance_state', 'obj_id'}
        data = {k: v for k, v in vars(self).items() if k not in excluded_fields}

        # 2. Lh 모델 생성 (obj_id는 Mixin의 default에 의해 자동생성됨)
        return AhLclMpmsProdInf(
            ref_obj_id=self.obj_id,  # 현재 Ln의 ID를 ref로 전달
            **data
        )


