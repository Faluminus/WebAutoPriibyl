from typing import Annotated
from pydantic import BaseModel, model_validator, constr, Field
from typing_extensions import Self
from uuid import UUID
from numpy.typing import NDArray
import numpy as np

#VARIABLE LENGTH CONSTS
MAX_LENGTH_NAME= 15
MAX_LENGTH_LAST_NAME= 20
MAX_LENGTH_MESSAGE = 400
MIN_LENGTH_MESSAGE = 15
MAX_LENGTH_USERNAME = 20
MAX_LENGTH_PASSWORD = 30
MAX_LENGTH_PART_NAME = 150
MAX_LENGTH_CAR_NAME = 80
EXACT_LENGTH_UUID = 36

#CLASS BEHAVIOR
class StringifyDeepestFilter(BaseModel):
    def __str__(self):
        for name, value in self.model_dump().items():
            if name == "itself":
                continue
            if value is not None:
                return str(name)
        return str(self.__class__.__name__)

    def __eq__(self, other):
        return str(self) == str(other)
    

#VALIDATIONS
class ParentReqCheck(BaseModel):
    @model_validator(mode='before')
    def check_if_parent_is_requested(self) -> Self | None:
        if self.itself is None:
            return None
        if self.itself:
            return self
        else:
            return None

class PickGroup(BaseModel):
    @model_validator(mode='after')
    def pick_group(self) -> Self | None:
        for name, value in self.model_dump().items():
            if name == "itself":
                continue
            if value is not None:
                return name, value
        return None

class Car(BaseModel):
    brand: str = Field(description="The name of the brand", max_length=50)
    model: str = Field(description="Model of the car", max_length=50)
    type: str = Field(description="Type of the model", max_length=50)

class FullCar(Car):
    engine: str = Field(description="Used engine in the car", max_length=50)
    engine_type: str | None = Field(default=None, description="Type of the engine", max_length=50)
    engine_volume: float | None = Field(default=None, gt=0, description="Volume of the engine")
    engine_kilowatts: int | None= Field(default=None, gt=0, description="Kilowatts of the engine")
    engine_horsepower: int | None = Field(default=None, gt=0, description="Horsepower of the engine")
    valves: Annotated[NDArray[np.int32], 2] = Field(default=None, description="Number of cylinders per valve and amount of valves")

class ListedPart(BaseModel):
    model_config = {"extra":"forbid"}
    id: int = Field(gt=0)
    price: float = Field(gt=0, default=0.0, description="The price of the part must be higher than 0.")
    name: str | None = Field(default=None, description="The name of the part.", max_length=50)
    fits: Car
    special_info: list[dict[str, str]] = Field(default=None, description="Specific info about the part")

class PartDetail(ListedPart):
    amount: int = Field(gt=0, default=0, description="The amount of the part must be higher than 0.")
    description: str | None = Field(default=None, description="Description of the part can contain 500 characters at maximum", max_length=500)
    fits: FullCar

class ListedCar(FullCar):
    model_config = {"extra": "forbid"}
    uuid: UUID = Field(default=None, description="UUID of the part", max_length=36)
    price: float = Field(gt=0, default=0.0, description="The price of the car must be higher than 0.")
    mileage: float = Field(gt=0, default=0.0, description="The mileage of the car must be higher than 0.")
    key_features: list[str]
    detail: list[str]
    car_state: list[str]

class CarDetail(ListedCar):
    model_config = {"extra": "forbid"}
    description: str = Field(description="Description of the part can contain 500 characters at maximum",
                             max_length=500)
    interior: list[str]
    exterior: list[str]
    infotainment: list[str]
    other: list[str]

#CAR FILTER
class CarsFilter(BaseModel):
    pass

#PART FILTER
#UNDERCARIAGE FILTERS
class BrzdovyTrmen(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    brzdovy_trmen_montaz: bool | None = None
    casti_brzdoveho_trmenu: bool | None = None

class BubnovaBrzda(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    brzdove_oblozeni_a_celisti: bool | None = None
    brzdovy_buben: bool | None = None
    brzdovy_valecek: bool | None = None
    opravna_sada: bool | None = None
    ovladani_tahla_a_prislusenstvi: bool | None = None
    parkovaci_brzda: bool | None = None
    prislusenstvi: bool | None = None

class KotoucovaBrzda(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    brzdove_desticky: bool | None = None
    brzdove_kotouce: bool | None = None
    prislusenstvi: bool | None = None
    souprava_brzda: bool | None = None

class BrzdoveSystemy(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    brzdova_kapalina: bool | None = None
    brzdove_hadicky: bool | None = None
    brzdove_potrubi: bool | None = None
    brzdovy_trmen: BrzdovyTrmen
    brzdovy_valecek: bool | None = None
    bubnova_brzda: BubnovaBrzda
    hlavni_brzdovy_valec: bool | None = None
    kotoucova_brzda: KotoucovaBrzda
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

class PricneTahloRizeni(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    jednotlive_dily: bool | None = None
    pricne_tahlo_rizeni: bool | None = None

class Rizeni(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    hadice_trubka: bool | None = None
    hlavni_paka_rizeni: bool | None = None
    chladic_oleje: bool | None = None
    manzeta_rizeni: bool | None = None
    meziulozeni_rizeni: bool | None = None
    olej: bool | None = None
    olejovy_tlakovy_spinac: bool | None = None
    prenosny_dil: bool | None = None
    pricne_tahlo_rizeni: PricneTahloRizeni
    rizeni_a_cerpadlo: bool | None = None
    skrin_rizeni: bool | None = None
    sloupek_rizeni: bool | None = None
    snimac_uhlu_rejdu: bool | None = None
    tahla_rizeni: bool | None = None
    tlumic_rizeni: bool | None = None
    volant: bool | None = None
    vyrovnavaci_nadrzka_oleje: bool | None = None
    zaveseni_rizeni: bool | None = None

class GumoveDorazyAPrachovky(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    prislusenstvi: bool | None = None
    vzpera: bool | None = None

class PruzinyTlumice(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    dily_podvozku: bool | None = None
    automaticke_vyrovnavani_vysky_vozidla: bool | None = None
    gumove_dorazy_a_prachovky: GumoveDorazyAPrachovky
    listova_pruzina: bool | None = None
    lozisko_vzpery: bool | None = None
    pruziny_podvozku: bool | None = None
    sroubovaci_podvozkove_dily: bool | None = None
    tlumice_perovani: bool | None = None
    ukazatel_zatizeni_napravy: bool | None = None
    vzduchove_odpruzeni: bool | None = None

class NabojALoziskoKola(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    naboj_kola: bool | None = None
    lozisko_kola: bool | None = None
    cep_napravy: bool | None = None
    tesnici_krouzek: bool | None = None
    ulozeni_pouzdra_loziska: bool | None = None

class NapravniceAUlozeni(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    silentblok_ulozeni_zadni_napravy: bool | None = None
    silentbloky_a_cepy_napravnice: bool | None = None
    silentbloky_nosniku_napravy: bool | None = None

class PricneRamenoAVymeneCasti(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    pricne_rameno: bool | None = None
    vymene_casti_pricneho_ramene: bool | None = None

class StabilizatorNapravyAJehoDily(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    kosti_a_tycky_stabilizatoru: bool | None = None
    tyc_stabilizatoru: bool | None = None
    ulozeni_stabilizatoru: bool | None = None
    zkrutna_tyc: bool | None = None

class SvislyCepNapravyAOpravneSady(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    opravna_sada: bool | None = None
    svisly_cep_napravy: bool | None = None
    sroub_svisleho_cepu: bool | None = None

class TahlaRizeniCepyRizeni(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    kloub_kolenove_paky: bool | None = None
    opravne_sady_kloubu_cepu_napravy: bool | None = None

class ZaveseniNapravy(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    naboj_a_lozisko_kola: NabojALoziskoKola
    napravnice_a_ulozeni: NapravniceAUlozeni
    pruzne_upevneni_a_loziska: bool | None = None
    pricna_vzpera_a_vzpera_pricneho_zavesneho_ramena: bool | None = None
    pricne_rameno_a_vymene_casti: PricneRamenoAVymeneCasti
    rozsireni_rozchodu: bool | None = None
    sada_ulozeni_a_zaveseni_kol: bool | None = None
    stabilizator_napravy_a_jeho_dily: StabilizatorNapravyAJehoDily
    svisly_cep_napravy_a_opravne_sady: SvislyCepNapravyAOpravneSady
    system_kontroly_tlaku_v_pneumatikach: bool | None = None
    tahla_rizeni_cepy_rizeni: TahlaRizeniCepyRizeni
    ulozeni_vzpery_napravy: bool | None = None

class Podvozek(StringifyDeepestFilter, PickGroup, ParentReqCheck, BaseModel):
    itself: bool | None = None
    brzdove_systemy: BrzdoveSystemy
    rizeni: Rizeni
    pruziny_a_tlumice: PruzinyTlumice
    zaveseni_napravy: ZaveseniNapravy

#ENGINE FILTERS
class Engine(BaseModel):
    engine: bool = False

class PartsFilter(PickGroup, BaseModel):
    model_config = {"extra":"forbid"}
    car: Car
    undercarriage: Podvozek
    engine: Engine

#USER
class BaseUser(BaseModel):
    username: Annotated[str, Field(max_length=MAX_LENGTH_USERNAME)]
    email: str

class UserIn(BaseUser):
    password: Annotated[str, Field(max_length=MAX_LENGTH_PASSWORD)]

class UserOut(BaseUser):
    pass

#FORM
class Form(BaseModel):
    name: Annotated[str, Field(max_length=MAX_LENGTH_NAME)]
    last_name: Annotated[str, Field(max_length=MAX_LENGTH_LAST_NAME)]
    email: Annotated[str, Field()]
    message: Annotated[str, Field(min_length=MIN_LENGTH_MESSAGE, max_length=MAX_LENGTH_MESSAGE)]