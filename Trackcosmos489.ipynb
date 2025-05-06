!pip install n2yo pandas matplotlib requests cartopy
import os import time import logging from dataclasses import dataclass from pathlib import Path from typing import Optional, Tuple

import requests import pandas as pd import matplotlib.pyplot as plt

@dataclass(frozen=True) class Config: API_KEY: str = "QH9F6F-C8SJM3-TCZ5Y3-3MZQ" NORAD_ID: int = 6073 LAT: float = 43.4977 LON: float = 0.9376 ALT_INIT: float = 200.0 CSV_FILE: Path = Path("cosmos482_data.csv") LOG_FILE: Path = Path("cosmos482_alert.log") IMPACT_PNG: Path = Path("cosmos482_impact.png") ALT_CRITICAL: float = 160.0 BASE_INTERVAL: int = 300 ALERT_INTERVAL: int = 60 MIN_PERSIST_POINTS: int = 5 PERSIST_ALTITUDE: float = 180.0 NB_POINTS_MOY: int = 178 MIN_LOSS_THRESHOLD: float = 0.001 ORBIT_DURATION_MIN: float = 89.0

logging.basicConfig( filename=Config.LOG_FILE, level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s" ) logger = logging.getLogger(name)

class N2YOClient: BASE_URL = "https://api.n2yo.com/rest/v1/satellite/positions"

def __init__(self, api_key: str):
    self.api_key = api_key
    self.session = requests.Session()
    self.session.params = {"apiKey": self.api_key}

def get_position(self, norad_id: int, lat: float, lon: float, alt: float) -> Optional[dict]:
    """
    Récupère la position actuelle du satellite via l'API N2YO.
    Retourne un dict avec 'timestamp', 'satlatitude', 'satlongitude', 'sataltitude'.
    """
    url = f"{self.BASE_URL}/{norad_id}/{lat}/{lon}/{alt}/1"
    try:
        response = self.session.get(url, timeout=10)
        response.raise_for_status()
        positions = response.json().get("positions", [])
        return positions[0] if positions else None
    except requests.RequestException as err:
        logger.error(f"Erreur API N2YO: {err}")
        return None

class DataStore: def init(self, csv_path: Path): self.csv_path = csv_path if csv_path.exists(): self.df = pd.read_csv(csv_path) else: cols = ["timestamp", "datetime_str", "latitude", "longitude", "altitude", "apogee", "perigee"] self.df = pd.DataFrame(columns=cols)

def append(self, record: dict) -> None:
    """
    Ajoute un enregistrement et sauvegarde le CSV.
    """
    new_row = pd.DataFrame([record])
    self.df = pd.concat([self.df, new_row], ignore_index=True)
    self.df.to_csv(self.csv_path, index=False)
    logger.info(f"Enregistrement ajouté: {record}")

class ReentryDetector: def init(self, df: pd.DataFrame, cfg: Config): self.df = df self.cfg = cfg

def detect(self) -> Optional[str]:
    """
    Renvoie un message si une condition de rentrée est détectée.
    """
    if self.df.empty:
        return None

    recent = self.df.tail(self.cfg.NB_POINTS_MOY)
    low_alt = recent[recent["altitude"] < self.cfg.PERSIST_ALTITUDE]
    if len(low_alt) >= self.cfg.MIN_PERSIST_POINTS:
        diffs = low_alt.index.to_series().diff().fillna(1)
        if diffs.max() == 1:
            return f"Altitude < {self.cfg.PERSIST_ALTITUDE} km persistante"

    perigees = self.df["perigee"].dropna()
    if len(perigees) >= 10:
        last10 = perigees.tail(10).to_list()
        if all(last10[i] > last10[i+1] for i in range(9)):
            return "Périgée en baisse continue"

    alts = recent["altitude"].dropna().to_list()
    if len(alts) >= 5:
        deltas = [alts[i+1] - alts[i] for i in range(len(alts)-1)]
        accels = [deltas[i+1] - deltas[i] for i in range(len(deltas)-1)]
        if len(accels) >= 3 and all(a < 0 for a in accels[-3:]):
            return "Perte d'altitude accélérée"
    return None

class ImpactEstimator: def init(self, df: pd.DataFrame, cfg: Config): self.df = df self.cfg = cfg

def estimate(self) -> Tuple[Optional[float], Optional[float]]:
    """
    Estime la latitude et longitude d'impact.
    """
    if len(self.df) < 2:
        return None, None

    p1, p2 = self.df.iloc[-2], self.df.iloc[-1]
    dt = p2["timestamp"] - p1["timestamp"]
    if dt <= 0:
        return None, None

    loss = p1["altitude"] - p2["altitude"]
    if loss <= self.cfg.MIN_LOSS_THRESHOLD:
        return None, None

    vlat = (p2["latitude"] - p1["latitude"]) / dt
    vlon = (p2["longitude"] - p1["longitude"]) / dt

    secs_left = (p2["altitude"] - self.cfg.ALT_CRITICAL) / loss * dt
    if secs_left < 0 or secs_left > 24 * 3600:
        return None, None

    lat_imp = max(-90, min(90, p2["latitude"] + vlat * secs_left))
    lon_imp = ((p2["longitude"] + vlon * secs_left + 180) % 360) - 180
    return lat_imp, lon_imp

class MapGenerator: def init(self, output_path: Path): self.output_path = output_path

def generate(self, lat: float, lon: float, region: str = "Inconnu", country: str = "Inconnu") -> None:
    """
    Trace la position estimée d'impact et sauvegarde le graphique.
    """
    plt.figure(figsize=(10, 5))
    plt.scatter([lon], [lat], s=50, c="red")
    plt.title(f"Zone d'impact estimée : {lat:.2f}°, {lon:.2f}° - {region}, {country}")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    plt.grid(True)
    plt.savefig(self.output_path)
    plt.close()
    logger.info(f"Carte d'impact sauvegardée : {self.output_path}")

class AlertManager: def alarm(self, message: str) -> None: """ Logue et affiche une alerte sonore. """ logger.warning(message) print(f"*** ALERTE *** {message}") for _ in range(5): print("\a", end="", flush=True) time.sleep(0.1)

class SatelliteReentryTracker: def init(self, cfg: Config): self.cfg = cfg self.api = N2YOClient(cfg.API_KEY) self.store = DataStore(cfg.CSV_FILE) self.alert_mgr = AlertManager() self.reentry_confirmed = False

def run_once(self) -> Optional[float]:
    pos = self.api.get_position(
        self.cfg.NORAD_ID,
        self.cfg.LAT,
        self.cfg.LON,
        self.cfg.ALT_INIT
    )
    if not pos:
        return None

    record = {
        "timestamp": pos["timestamp"],
        "datetime_str": pd.to_datetime(pos["timestamp"], unit="s").strftime("%Y-%m-%d %H:%M:%S"),
        "latitude": pos["satlatitude"],
        "longitude": pos["satlongitude"],
        "altitude": pos["sataltitude"],
        "apogee": max(self.store.df.get("apogee", [pos["sataltitude"]]) + [pos["sataltitude"]]),
        "perigee": min(self.store.df.get("perigee", [pos["sataltitude"]]) + [pos["sataltitude"]]),
    }
    self.store.append(record)
    print(f"{record['datetime_str']} | Alt: {record['altitude']:.1f} km")

    msg = ReentryDetector(self.store.df, self.cfg).detect()
    if msg and not self.reentry_confirmed:
        self.reentry_confirmed = True
        lat_imp, lon_imp = ImpactEstimator(self.store.df, self.cfg).estimate()
        if lat_imp is not None and lon_imp is not None:
            MapGenerator(self.cfg.IMPACT_PNG).generate(lat_imp, lon_imp)
        self.alert_mgr.alarm(f"Début de rentrée détecté ({msg})")

    return record["altitude"]

def run(self) -> None:
    print("=== Surveillance de Cosmos 482 ===")
    while True:
        alt = self.run_once()
        interval = (
            self.cfg.ALERT_INTERVAL
            if alt is not None and alt < self.cfg.ALT_CRITICAL
            else self.cfg.BASE_INTERVAL
        )
        time.sleep(interval)

if name == "main": tracker = SatelliteReentryTracker(Config) tracker.run()

