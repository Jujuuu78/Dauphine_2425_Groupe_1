import json
import os
import uuid
from typing import Optional
from uuid import UUID

from domain.model.historic import Historic
from domain.model.interaction import Interaction


class HistoricRepository:
    def __init__(self, path_json_file: str):
        self.path_json_file = path_json_file
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.path_json_file):
            with open(self.path_json_file, "w") as f:
                json.dump({}, f)

    def save(self, interaction: Interaction, id_historic: Optional[UUID] = None):
        with open(self.path_json_file, "r+") as f:
            try:
                data = json.load(f)  # Charger les données existantes
            except json.JSONDecodeError:
                data = {}  # Si le fichier est vide ou corrompu, réinitialiser

            if id_historic is None:
                id_historic = uuid.uuid4()
                historic = Historic(id=id_historic, interactions=[interaction])
            else:
                historic_data = data.get(str(id_historic), {"interactions": []})
                interactions = [Interaction(**i) for i in historic_data["interactions"]]
                interactions.append(interaction)
                historic = Historic(id=id_historic, interactions=interactions)

            # Mise à jour du dictionnaire avec le nouvel historique
            data[str(id_historic)] = historic.model_dump()
            print(data)

            # Réécriture complète du fichier en sérialisant correctement les UUID
            f.seek(0)

            # Fonction personnalisée pour sérialiser UUID
            def uuid_serializer(obj):
                if isinstance(obj, UUID):
                    return str(obj)
                raise TypeError("Type not serializable")

            json.dump(data, f, indent=4, default=uuid_serializer)
            f.truncate()  # Efface l'ancien contenu restant

            return historic

    def get(self, id_historic: UUID) -> Optional[Historic]:
        with open(self.path_json_file, "r") as f:
            data = json.load(f)
            historic_data = data.get(str(id_historic))
            if historic_data:
                return Historic(**historic_data)
        return None
