from django.core.management.base import BaseCommand
from travelapp.models import CityDetail, Travel
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Import data from Excel file to YourModel'

    def handle(self, *args, **options):
        BASE2_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        excel_file_path = os.path.join(BASE2_DIR, 'management', 'commands', 'locationlist.xlsx')

        try:
            data = pd.read_excel(excel_file_path, sheet_name='Sheet1')
            for index, row in data.iterrows():
                try:
                    city_detail = CityDetail.objects.get(
                       
                        city=row['city'],
                        detail=row['detail'],
                        # 모델의 다른 필드들도 추가
                    )
                except CityDetail.DoesNotExist:
                    city_detail = CityDetail.objects.create(
                        city=row['city'],
                        detail=row['detail'],
                        # 모델의 다른 필드들도 추가
                    )

                # Travel.objects.create(
                #     city_detail=city_detail
                # )

            self.stdout.write(self.style.SUCCESS('Successfully imported data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to import data: {str(e)}'))
