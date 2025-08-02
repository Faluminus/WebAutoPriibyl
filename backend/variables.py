from typing import Annotated
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self
from uuid import UUID
from numpy.typing import NDArray
import numpy as np

class Car(BaseModel):
    brand: str = Field(description="The name of the brand", max_length=50)
    model: str = Field(description="Model of the car", max_length=50)
    type: str = Field(description="Type of the model", max_length=50)
    engine: str = Field(description="Used engine in the car", max_length=50)
    engine_type: str = Field(default=None, description="Type of the engine", max_length=50)
    engine_volume: float = Field(default=None, qt=0, description="Volume of the engine")
    engine_kilowatts: int = Field(default=None, qt=0, description="Kilowatts of the engine")
    engine_horsepower: int = Field(default=None, qt=0, description="Horsepower of the engine")
    valves: Annotated[NDArray[np.int32], 2] = Field(default=None, description="Number of cylinders per valve and amount of valves")

class Part(BaseModel):
    model_config = {"extra":"forbid"}
    uuid: UUID = Field(default=None, description="UUID of the part", max_length=36)
    price: float = Field(qt=0, default=0.0, description="The price of the part must be higher than 0.")
    amount: int = Field(qt=0, default=0, description="The amount of the part must be higher than 0.")
    name: str = Field(default=None, description="The name of the part.", max_length=50)
    description: str | None = Field(default=None, description="Description of the part can contain 500 characters at maximum", max_length=500)
    fits: Car
    special_info: list[dict[str, str]] = Field(default=None, description="Specific info about the part")

class ListedCar(Car):
    model_config = {"extra": "forbid"}
    uuid: UUID = Field(default=None, description="UUID of the part", max_length=36)
    price: float = Field(qt=0, default=0.0, description="The price of the car must be higher than 0.")
    mileage: float = Field(qt=0, default=0.0, description="The mileage of the car must be higher than 0.")
    description: str = Field(description="Description of the part can contain 500 characters at maximum", max_length=500)
    key_features: list[str]
    detail: list[str]
    motor: list[str]
    car_state: list[str]
    interior: list[str]
    exterior: list[str]
    infotainment: list[str]
    other: list[str]

class CarsFilter(BaseModel):
    pass

#UNDERCARIAGE FILTERS
class BrzdoveSystemy(BaseModel):
    itself: bool | None = None
    brzdova_kapalina: bool | None = None
    brzdove_hadicky: bool | None = None
    brzdove_potrubi: bool | None = None
    brzdovy_trmen: bool | None = None
    bubnova_brzda: bool | None = None
    hlavni_brzdovy_valec: bool | None = None
    kotoucova_brzda: bool | None = None
    brzdove_desticky: bool | None = None
    brzdove_kotouce: bool | None = None
    nadrz_na_brzdovou_kapalinu: bool | None = None
    paky_a_brzdova_lanka: bool | None = None
    parkovaci_brzda: bool | None = None
    podtlakove_cerpadlo: bool | None = None
    posilovac_brzd: bool | None = None
    regulace_jizdni_dynamiky: bool | None = None
    regulator_brzdne_sily: bool | None = None
    simulator_pocitu_z_brzdoveho_pedalu: bool | None = None
    spinac_brzdoveho_svetla: bool | None = None
    tlakovy_aukumulator_a_spinac: bool | None = None
    ukazatel_opotrebeni: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


class Rizeni(BaseModel):
    itself: bool | None = None
    hadice_trubka: bool | None = None
    hlavni_paka_rizeni: bool | None = None
    chladic_oleje: bool | None = None
    manzeta_rizeni: bool | None = None
    meziulozeni_rizeni: bool | None = None
    olej: bool | None = None
    olejovy_tlakovy_spinac: bool | None = None
    prenosny_dil: bool | None = None
    pricne_tahlo_rizeni: bool | None = None
    rizeni_a_cerpadlo: bool | None = None
    skrin_rizeni: bool | None = None
    sloupek_rizeni: bool | None = None
    snimac_uhlu_rejdu: bool | None = None
    tahla_rizeni: bool | None = None
    tlumic_rizeni: bool | None = None
    volant: bool | None = None
    vyrovnavaci_nadrzka_oleje: bool | None = None
    zaveseni_rizeni: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


class PruzinyTlumice(BaseModel):
    itself: bool | None = None
    dily_podvozku: bool | None = None
    automaticke_vyrovnavani_vysky_vozidla: bool | None = None
    gumove_dorazy_a_prachovky: bool | None = None
    listova_pruzina: bool | None = None
    lozisko_vzpery: bool | None = None
    pruziny_podvozku: bool | None = None
    sroubovaci_podvozkove_dily: bool | None = None
    tlumice_perovani: bool | None = None
    ukazatel_zatizeni_napravy: bool | None = None
    vzduchove_odpruzeni: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None

class NabojALoziskoKola(BaseModel):
    itself: bool | None = None
    naboj_kola: bool | None = None
    lozisko_kola: bool | None = None
    cep_napravy: bool | None = None
    tesnici_krouzek: bool | None = None
    ulozeni_pouzdra_loziska: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


class NapravniceAUlozeni(BaseModel):
    itself: bool | None = None
    silentblok_ulozeni_zadni_napravy: bool | None = None
    silentbloky_a_cepy_napravnice: bool | None = None
    silentbloky_nosniku_napravy: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None

class PricneRamenoAVymeneCasti(BaseModel):
    itself: bool | None = None
    pricne_rameno: bool | None = None
    vymene_casti_pricneho_ramene: bool | None = None

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


class StabilizatorNapravyAJehoDily(BaseModel):
    itself: bool = False
    kosti_a_tycky_stabilizatoru: bool = False
    tyc_stabilizatoru: bool = False
    ulozeni_stabilizatoru: bool = False
    zkrutna_tyc: bool = False

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


class ZaveseniNapravy(BaseModel):
    itself: bool = False
    naboj_a_lozisko_kola: NabojALoziskoKola
    napravnice_a_ulozeni: NapravniceAUlozeni
    pruzne_upevneni_a_loziska: bool = False
    pricna_vzpera_a_vzpera_pricneho_zavesneho_ramena: bool = False
    pricne_rameno_a_vymene_casti: PricneRamenoAVymeneCasti
    rozsireni_rozchodu: bool = False
    sada_ulozeni_a_zaveseni_kol: bool = False
    stabilizator_napravy_a_jeho_dily: StabilizatorNapravyAJehoDily

    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None

class Podvozek(BaseModel):
    itself: bool = False
    brzdove_systemy: BrzdoveSystemy
    rizeni: Rizeni
    pruziny_a_tlumice: PruzinyTlumice
    zaveseni_napravy: ZaveseniNapravy
    @model_validator(mode='after')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None


#ENGINE FILTERS
class Engine(BaseModel):
    engine: bool = False



class PartsFilter(BaseModel):
    model_config = {"extra":"forbid"}
    car: Car
    undercarriage: Podvozek
    engine: Engine

    @model_validator(mode='after')
    def pick_group(self) -> Self | None:
        for _, value in self.model_dump().items():
            if value is not None:
                return value



class BaseUser(BaseModel):
    username: str
    email: str

class UserIn(BaseUser):
    password: str

class UserOut(BaseUser):
    pass