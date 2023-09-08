from django.http import JsonResponse
def update_employee(request,id,employee_name,employee_salary,employee_age):
    list=[]
    print(request)
    message="Successfuly updated"
    message={"message":message}
    return JsonResponse(message)

def GetLearnerAssessments(request):
    data={"data":{"getLearnerAssessments":{"statusCode":200,"body":"{\"Items\":[]}","Message":"null","errorMessage":"null","errorType":"null","userSelectedCourses":"null"}}}

    return JsonResponse(data)
    
def getTeacherDetails(request):
    data={"data":{"getTeacherDetails":"{\"statusCode\":200,\"message\":\"Authenticated user\"}"}}

    return JsonResponse(data)
def GetGroupSessionInfo(request):
    data={
  "data": {
    "getGroupSessionLearnerInfo": {
      "course": 612,
      "endTime": 1612179000,
      "id": 4490,
      "isFlipped": "True",
      "sessionCalendarType": "online",
      "sessionType": "course",
      "startTime": 1612177200,
      "status": "finished",
      "students": [
        {
          "classroomLink": "https://ctmsdev01-tms.learnship.today/v2/classroom/index?id=f7a74d05c78be8e859dec82a08eb303f",
          "guid": "c33bccbe-2fcd-46d9-abf0-90a8074cd603",
          "id": 417792,
          "name": "LNSprintGerman1130028, FNSprintGerman028",
          "onBoardingStatus": "null",
          "organization": {
            "id": 417234,
            "name": "Sprint Business Languages"
          },
          "role": "1"
        }
      ],
      "teacher": {
        "id": 158448,
        "name": "TeacherFr, Hr",
        "organization": "",
        "role": "2"
      },
      "trainingMethod": "online",
      "trainingType": "oup_level"
    }
  }
}

    return JsonResponse(data)
def GetPeopleInformation(request):
    data={"data":{"getpeopleInformation":{"edgeUid":1712118,"geId":"2084169","username":"testguide01","firstName":"Test","lastName":"Guide","email":"vijay.munuswamy@learnship.com"}}}

    return JsonResponse(data)
def getCourseSessionMapping(request):
    data={"data":{"getCourseSessionMapping":"{\"userBasicDetails\":{\"isGroupSession\":false,\"sprintLanguage\":\"German\",\"userId\":1725600,\"licenseId\":1459407,\"uuid\":\"c33bccbe-2fcd-46d9-abf0-90a8074cd603\",\"productType\":\"oup_level\",\"geId\":2097955,\"geUuid\":\"C33BCCBE-2FCD-46D9-ABF0-90A8074CD603\",\"userName\":\"1130SprintGerman028\",\"email\":\"dhivyalakshmi.senthilkumar@learnship.com\",\"firstName\":\"FNSprintGerman028\",\"lastName\":\"LNSprintGerman1130028\",\"licenseStartDate\":1652844780,\"licenseEndDate\":1683331200,\"sessionInfo\":{\"status\":1,\"frequency\":4,\"duration\":30,\"frequencyUnit\":1,\"type\":12,\"reschedulingNoticeHours\":6,\"reschedulingLimit\":50,\"CanReschedulingOnDemand\":1,\"TotalSessions\":11},\"accountId\":108872,\"isHalo\":true,\"courseId\":612,\"isOnBoardingCompleted\":true,\"level\":\"A2.1\",\"courseLevel\":\"A2.1\",\"levelType\":0,\"LevelDescription\":\"Admin Designated Level\",\"LevelChange\":-1,\"skipRedoCount\":0},\"courseMapping\":[{\"moduleId\":\"30c4f4eb-b66f-4ea8-9afe-f5abaed0a560\",\"title\":\"Geschäftsverhandlungen\",\"level\":\"A2.1\",\"coursePart\":{\"id\":\"56862b4a-60ed-4c4b-ad76-a682a57fe6d4\",\"slug\":\"a\",\"title\":\"A\"},\"units\":[{\"unitId\":\"5b6eb631-e21b-4e1b-8780-964c3b8188fd\",\"title\":\"Projektleitung\",\"activityDetails\":{\"id\":\"11e5b55f-fff5-45c8-9512-4dcc2c0da9b6\",\"title\":\"Projektleitung\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"95f8f987-e104-4d89-80f8-827034d4206e\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"dd0a8f79-7310-446d-a686-4d478809fe7d\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"77c5cf66-54b0-4cfd-af1a-1b251ba50ab0\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"dfc9e38d-af9e-489d-935e-1af914643a7a\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"0b3652d7-d403-45ff-a7a0-e490cc930492\",\"title\":\"Übung 4\",\"type\":\"fillinthegapsselect\"},{\"id\":\"15cd2073-b917-4b2e-b8ae-3598dbb034e2\",\"title\":\"Übung 5\",\"type\":\"fillinthegapsclick\"},{\"id\":\"6d3e4909-8b69-4260-83dc-1128e4b1be91\",\"title\":\"Übung 6\",\"type\":\"wordselector\"},{\"id\":\"7e76a1dc-910d-4ec0-8dee-3652754ab4c7\",\"title\":\"Übung 7\",\"type\":\"fillinthegapstext\"},{\"id\":\"1f00e568-719c-486f-8bbe-42512f4bb2d5\",\"title\":\"Übung 8 \",\"type\":\"choice\"},{\"id\":\"e29d2359-2dd9-4caf-add6-0991878669d0\",\"title\":\"Übung 9 (A)\",\"type\":\"sentence\"},{\"id\":\"7c583a67-5f3c-466b-9560-1ec5be157a9d\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"af3193cf-b23f-4984-909f-b4db0de6f2fd\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":11,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"cfe450a9-a169-41ce-9621-1f4038dba6d5\",\"title\":\"Der/Die Lernende kann in Standardsprache Verhandlungen führen und dabei die Meinung ausdrücken, zustimmen und ablehnen und die Verhandlung zusammenfassen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"73afc3cd-1f51-445b-90ad-1c89cada71b6\",\"title\":\"Der/Die Lernende kann die Modalverben „können“, „dürfen“ und „sollen/sollten“ korrekt anwenden.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; a) Geschäftsverhandlungen &gt; 1. Projektleitung</p><p>Instructions can be found in the attached trainer notes in the classroom</p>\",\"sessionDetails\":{\"id\":4490,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612177200,\"endTime\":1612179000,\"course\":612}},{\"unitId\":\"9a10cc04-53bc-4f91-9fe7-922cf5f43e92\",\"title\":\"Problembewältigung\",\"activityDetails\":{\"id\":\"86d73c1d-0661-46c7-97de-d776b9c7aba6\",\"title\":\"Problembewältigung\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"a51f8c98-84bb-4276-8dfe-f5e96540692a\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"b57e1dc4-74d5-41ad-a9cb-981a5ae977b7\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"76a39eb6-c037-4c0a-afa8-dc4a64206411\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"f4f8e8df-2eb2-48fb-a482-0db3f71981cc\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"1e030e61-3fd7-43e2-a521-65d14ca2bdc4\",\"title\":\"Grammatik-Video\",\"type\":\"video\"},{\"id\":\"ee9183b2-69db-45ae-9eca-a8d9d25678f9\",\"title\":\"Übung 4\",\"type\":\"fillinthegapsclick\"},{\"id\":\"84fdc11b-c2ae-4d02-bee5-a76318a2ddf7\",\"title\":\"Übung 5 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"aa328423-8a39-4518-8ca3-5ecd4cde18cd\",\"title\":\"Übung 6 \",\"type\":\"wordselector\"},{\"id\":\"34fb3b5b-a030-451d-ac25-52ffd984de69\",\"title\":\"Übung 7\",\"type\":\"fillinthegapstext\"},{\"id\":\"f5ddb0b3-0b4f-4846-9f1f-a6c9e225d488\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapstext\"},{\"id\":\"a84c5fa6-e23f-4b9c-ba13-bdd2933dcf35\",\"title\":\"Übung 9 (A) \",\"type\":\"sentence\"},{\"id\":\"9dd06f10-45f3-45ad-ae13-bbdee091ced3\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"95d6cd1c-f8cc-40cd-83cf-52f02e2cd8b8\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"0bade4d7-c978-417b-920f-5d830ccf372c\",\"title\":\"Der/Die Lernende kann einfache Ausdrücke, um zu überzeugen, einen Kompromiss zu schließen und eine Einigung zu erreichen, nutzen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"5ac299f3-d096-4b90-bf48-f6548bdd6a41\",\"title\":\"Der/Die Lernende kann den Konjunktiv II der Verben „haben“ und „sein“, der Modalverben und der Verben mit Hilfsverb „werden“ anwenden.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; a) Geschäftsverhandlungen &gt; 2. Problembewältigung</p><p>Instructions can be found in the attached trainer notes in the classroom</p>\",\"sessionDetails\":{\"id\":4491,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612263600,\"endTime\":1612265400,\"course\":612}},{\"unitId\":\"a9e1ad85-965c-4720-b96e-d26eae44faa7\",\"title\":\"Erteilung von Feedback\",\"activityDetails\":{\"id\":\"02f1a12d-9e3c-4328-aeb7-9238858884ef\",\"title\":\"Erteilung von Feedback\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"a9082a33-240d-48ae-9904-866ea6d46ce7\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"95d350b3-2864-493d-937e-0d2a058c8f49\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"bb840a58-b1e8-488b-aa42-4164ec7ee988\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"e5378079-97d3-4b80-8740-0c089c3fde28\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"93f4d518-155d-49e1-b0fb-54f72a50c91a\",\"title\":\"Übung 4\",\"type\":\"wordselector\"},{\"id\":\"9b2b1565-b07d-4f5a-8849-cb4207d50cbc\",\"title\":\"Übung 5\",\"type\":\"fillinthegapsselect\"},{\"id\":\"46669cf4-4627-4512-8b17-386bdb46e689\",\"title\":\"Übung 6 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"3a12f09c-8107-4d40-9030-fe558642bbeb\",\"title\":\"Übung 7\",\"type\":\"fillinthegapsclick\"},{\"id\":\"3cad9257-8ae4-416a-80b7-426f3da5b62c\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapstext\"},{\"id\":\"5ba40f00-e968-489a-a836-f896bb34eccf\",\"title\":\"Übung 9 (A) \",\"type\":\"sentence\"},{\"id\":\"99930749-16ac-4297-91bc-490567d9290e\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"e7c1f02c-4bdf-4606-baa8-03d46cd81e3d\",\"title\":\"Übung 9 (C)\",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":11,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"3d02f51c-17b9-48c6-8277-e60baf492f15\",\"title\":\"Der/Die Lernende kann Standardsprache verwenden, um Angebote zu machen, auf Angebote zu antworten und eine Einigung zu erreichen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"e726f53d-c0fd-42d2-bfca-8d8fdd97b8ae\",\"title\":\"Der/Die Lernende kann Präpositionen, die von einem Dativ gefolgt werden, korrekt anwenden.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; a) Geschäftsverhandlungen &gt; 3. Erteilung von Feedback</p><p>Instructions can be found in the attached trainer notes in the classroom</p>\",\"sessionDetails\":{\"id\":4492,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612350000,\"endTime\":1612351800,\"course\":612}},{\"unitId\":\"62de0a9c-3992-4623-8bbe-9604d0db77d9\",\"title\":\"Mitarbeiterführung\",\"activityDetails\":{\"id\":\"b068267d-4af3-49fd-a8d6-02f856d8f523\",\"title\":\"Mitarbeiterführung\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"46ec33dc-7a65-409c-938d-d7d2f3b01b30\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"6c8d74b2-555a-4d54-a1d2-e74515df9eb7\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"fe2f4750-a2e5-4085-98b9-0c6ca8bc241b\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"77449fbb-eee8-488a-be81-06aa976a5fbb\",\"title\":\"Übung 3 \",\"type\":\"wordscategorizing\"},{\"id\":\"7ff9afe8-1355-4a16-b575-7cd5bef1114d\",\"title\":\"Grammatik-Video\",\"type\":\"video\"},{\"id\":\"137ec5c4-b0f0-49fd-a44c-55fd54844cbb\",\"title\":\"Übung 4 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"09f4b30e-6af6-4a8d-b6cc-b5707a1e363a\",\"title\":\"Übung 5 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"8f3dd17e-1f15-4914-a65d-d69bd553c1e5\",\"title\":\"Übung 6 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"6216c3cf-1129-463d-b911-089d33d5ca79\",\"title\":\"Übung 7\",\"type\":\"wordselector\"},{\"id\":\"4399c232-83e7-4440-be13-d4f47c66d1d5\",\"title\":\"Übung 8\",\"type\":\"fillinthegapsclick\"},{\"id\":\"3163acc9-d859-47f3-ab8d-76936e2f3a71\",\"title\":\"Übung 9 (A)\",\"type\":\"sentence\"},{\"id\":\"dec533b5-b6e5-4c5c-abc2-b4c193a7c9b4\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"33e5bc94-5a20-4438-965f-b61b1d59ff7f\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"f9473d49-7572-4b30-8f10-1d8a92c9b9f9\",\"title\":\"Der/Die Lernende kann Standardsprache verwenden, um andere Sichtweisen aufzuzeigen und andere zu bitten diese mitzutragen und kann über die Langzeitwirkung von Entscheidungen sprechen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"6be39499-04d5-40d8-a2e6-cb98ff3dc360\",\"title\":\"Der/Die Lernende kann das Prinzip der direkten und indirekten Fragen anwenden und diese richtig formulieren.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; a) Geschäftsverhandlungen &gt; 4. Mitarbeiterführung</p><p>Instructions can be found in the attached trainer notes in the classroom</p>\",\"sessionDetails\":{\"id\":4493,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612436400,\"endTime\":1612438200,\"course\":612}},{\"unitId\":\"f63a5fec-38f6-45a2-aa59-07eb345008ec\",\"title\":\"Rückblick\",\"activityDetails\":{\"id\":\"63c7ab2c-44f2-4aa1-917c-3b1fb3310b41\",\"title\":\"Rückblick\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"3ecf8380-4a1d-426e-a5f3-50bb5070c6ed\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"74f7d4ca-c607-43b0-865b-b0b71e039596\",\"title\":\"Übung 1 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"6d514ec8-64bc-41dc-a4ab-b5442aeb9be4\",\"title\":\"Übung 2 (A) \",\"type\":\"sentence\"},{\"id\":\"227c3c09-d377-41ab-9269-a545b6a08f2f\",\"title\":\"Übung 2 (B) \",\"type\":\"sentence\"},{\"id\":\"a7da851e-02fe-4fd9-b546-aa5ba3b3bcbd\",\"title\":\"Übung 2 (C)\",\"type\":\"sentence\"},{\"id\":\"8b2a35ae-ce77-48dd-bf82-7b853cbccfc4\",\"title\":\"Übung 2 (D) \",\"type\":\"sentence\"},{\"id\":\"a887dc2e-6881-4600-b17e-60cde0f1add6\",\"title\":\"Übung 3 \",\"type\":\"fillinthegapstext\"},{\"id\":\"e699881e-4b5c-445d-98c2-42622ef5877b\",\"title\":\"Übung 4\",\"type\":\"fillinthegapstext\"},{\"id\":\"25d29125-8e66-45b2-8535-9015b33d9237\",\"title\":\"Übung 5\",\"type\":\"wordscategorizing\"},{\"id\":\"87382469-2fc3-481b-965a-5987cb5d2ab9\",\"title\":\"Übung 6\",\"type\":\"fillinthegapsclick\"},{\"id\":\"0ecbd66c-f2a2-4538-a384-c2b92f3868a7\",\"title\":\"Übung 7 \",\"type\":\"fillinthegapstext\"},{\"id\":\"1ea3a71e-8496-4211-8178-d7448cd1f3d2\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapsselect\"}],\"vocabularyList\":null,\"totalExercises\":11,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"b3d0acbb-a028-4364-86c3-521b3d9dddf8\",\"title\":\"Der/Die Lernende hat den Wortschatz und den Sprachgebrauch gemeistert, um auf A2.1-Niveau über Geschäftsverhandlungen zu sprechen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"99b7a61e-99da-4fd0-b934-d295d922622e\",\"title\":\"Der/Die Lernende hat die Grammatik gemeistert, um auf A2.1-Niveau über Geschäftsverhandlungen zu sprechen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; a) Geschäftsverhandlungen &gt; 5. Rückblick</p><p>Instructions can be found in the attached trainer notes in the classroom</p>\",\"sessionDetails\":{\"id\":4494,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612522800,\"endTime\":1612524600,\"course\":612}}]},{\"moduleId\":\"fb7ac783-6c83-45dc-b30f-f4730220cefb\",\"title\":\"Geschäftspräsentationen\",\"level\":\"A2.1\",\"coursePart\":{\"id\":\"56862b4a-60ed-4c4b-ad76-a682a57fe6d4\",\"slug\":\"a\",\"title\":\"A\"},\"units\":[{\"unitId\":\"8c4cd40f-299f-47b5-b4b0-9cb12ba954e5\",\"title\":\"Eröffnung einer Präsentation\",\"activityDetails\":{\"id\":\"4ded9474-dc64-4aea-b3ff-d39aa1358aa4\",\"title\":\"Eröffnung einer Präsentation\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"824bf594-7bf9-4200-aa77-3326f6574982\",\"title\":\"Lernziele \",\"type\":\"index\"},{\"id\":\"d5d062e5-ea7b-4ed4-9ca4-3fa071f20115\",\"title\":\"Übung 1\",\"type\":\"choice\"},{\"id\":\"d6d13778-ce23-4087-98c6-22d50b9d344c\",\"title\":\"Übung 2\",\"type\":\"fillinthegapsclick\"},{\"id\":\"a9ae8810-3b3d-4cf9-a87c-c2107172527d\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"394d6177-e230-4edf-9dfc-92d14faf1e59\",\"title\":\"Grammatik-Video\",\"type\":\"video\"},{\"id\":\"d847bb9f-b8df-4887-97ac-56df9edaf5a2\",\"title\":\"Übung 4\",\"type\":\"fillinthegapsclick\"},{\"id\":\"5a9f03c6-d1ab-4ede-9afb-cfd1d91f1ebb\",\"title\":\"Übung 5\",\"type\":\"wordselector\"},{\"id\":\"164f6c21-3763-4e8a-945c-bb458b9d3266\",\"title\":\"Übung 6\",\"type\":\"fillinthegapsselect\"},{\"id\":\"c28ecfde-f69b-46ad-840e-b307789dff33\",\"title\":\"Übung 7\",\"type\":\"fillinthegapstext\"},{\"id\":\"00225d82-b21d-4f92-a66f-56c30b5a1ac9\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"8aab6866-2eb9-45dc-bf61-dc675bd39228\",\"title\":\"Übung 9 (A)\",\"type\":\"sentence\"},{\"id\":\"79c2c2fb-5061-41aa-aceb-7cd01ec8a0e0\",\"title\":\"Übung 9 (B)\",\"type\":\"sentence\"},{\"id\":\"0d2554f1-84e5-4ab0-93b7-b741cbe48917\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"f45fb673-368e-4823-9e93-616b91966240\",\"title\":\"Der/Die Lernende kann in einfacher Sprache eine Präsentation eröffnen, die Kennenlernrunde leiten und die Struktur der Präsentation erklären.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"ecef8cb6-1b21-40b9-86eb-7acefaaa85dd\",\"title\":\"Der/Die Lernende kann Reflexivpronomen verwenden und kann reflexive und reziproke Verben benutzen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; b) Geschäftspräsentation &gt; 1. Eröffnung einer Präsentation</p><p>Instructions can be found in the attached trainer notes in the classroom.</p>\",\"sessionDetails\":{\"id\":4495,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612609200,\"endTime\":1612611000,\"course\":612}},{\"unitId\":\"de4d4261-9aec-47f6-8196-3659fb9232fe\",\"title\":\"Klare Kommunikation\",\"activityDetails\":{\"id\":\"21e9d239-7f25-4b61-9772-e5229658a26e\",\"title\":\"Klare Kommunikation\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"d8d36a26-bfda-442b-bba2-6429ef686a66\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"8c9e287c-7ed0-4334-b569-c7a8e05f97b7\",\"title\":\"Übung 1\",\"type\":\"choice\"},{\"id\":\"915b68f6-2fb1-4896-9824-3b446be8cc66\",\"title\":\"Übung 2\",\"type\":\"fillinthegapstext\"},{\"id\":\"c87ca3a4-0b74-4fe5-beb7-ac85e2aaa0d3\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"25e6d68c-6558-446b-bba8-46cced31ecd7\",\"title\":\"Übung 4\",\"type\":\"wordselector\"},{\"id\":\"40cdbf61-f520-428d-965f-cc05bf6f7e1e\",\"title\":\"Übung 5\",\"type\":\"fillinthegapsselect\"},{\"id\":\"55d2c762-0d30-4708-ad33-e0c8c92317fd\",\"title\":\"Grammatik-Video\",\"type\":\"video\"},{\"id\":\"23568aaa-5d0e-4900-af0b-489b4b21df04\",\"title\":\"Übung 6\",\"type\":\"fillinthegapsclick\"},{\"id\":\"3c602c0a-1360-4e83-9e5b-c87bdf4eba7e\",\"title\":\"Übung 7 \",\"type\":\"wordscategorizing\"},{\"id\":\"4b6c280c-452c-40d5-817d-c03540394750\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapstext\"},{\"id\":\"4289fe45-951c-4a64-b2c0-6bbd28100a99\",\"title\":\"Übung 9 (A)\",\"type\":\"sentence\"},{\"id\":\"75f6297b-a9fd-4439-8794-2a4cbefd671e\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"b5874655-ee4b-4b7d-ba08-11965642ab22\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"83c722fd-3040-443d-8820-92f95c42004d\",\"title\":\"Der/Die Lernende kann in einfacher Sprache das Für und Wider unterschiedlicher Aspekte präsentieren.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"918696f7-6a0c-4440-875a-94bd0b6a8422\",\"title\":\"Der/Die Lernende kann die Präsensform und das Partizip II von häufig verwendeten unregelmäßigen Verben anwenden und kann Komparativ und Superlativ einsetzen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; b) Geschäftspräsentation &gt; 2. Klare Kommunikation</p><p>Instructions can be found in the attached trainer notes in the classroom.</p>\",\"sessionDetails\":{\"id\":4496,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612695600,\"endTime\":1612697400,\"course\":612}},{\"unitId\":\"9e32f1c7-068a-4e48-bfdf-4eb46f5a7f3c\",\"title\":\"Problembewältigung\",\"activityDetails\":{\"id\":\"96658732-a48c-48d3-a103-f93dd0e13523\",\"title\":\"Problembewältigung\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"7e45c8f0-03da-4202-9870-29cf1b6447b7\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"678cef35-05be-4077-810d-18f55204c3f6\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"bc0f3313-c4ca-4041-8e78-79dd73336f08\",\"title\":\"Übung 2\",\"type\":\"fillinthegapsclick\"},{\"id\":\"c14bdcde-c1b1-4389-b31d-3eb99126e603\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"acf99944-7c52-4e02-9efd-bee8b7902880\",\"title\":\"Übung 4\",\"type\":\"fillinthegapsclick\"},{\"id\":\"1520d0fa-d5cb-42a3-9b54-ec4baa1cec17\",\"title\":\"Grammatik-Video\",\"type\":\"video\"},{\"id\":\"f8c474c6-9f24-4f4a-8f82-7389dfa60ffa\",\"title\":\"Übung 5\",\"type\":\"choice\"},{\"id\":\"26a50699-0506-4ed5-aa01-f7c7e2df152a\",\"title\":\"Übung 6 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"cc2ac130-4742-4d6c-86d0-743b5b191968\",\"title\":\"Übung 7\",\"type\":\"wordselector\"},{\"id\":\"852d2740-15ee-443d-934f-59a7d37d929c\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapstext\"},{\"id\":\"26bbe122-5c72-4093-8fc7-c5bba2404bdc\",\"title\":\"Übung 9 (A) \",\"type\":\"sentence\"},{\"id\":\"cbba68d6-abb6-48f4-9c27-5d6871adb2de\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"8dd77d29-5108-4485-a69b-355bf7547afe\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"7c3fff37-7c9a-4a4c-a8d7-aa1e9454dcdc\",\"title\":\"Der/Die Lernende kann einfache Phrasen nutzen, um Informationen zu präsentieren, Probleme zu erklären und Lösungen vorzuschlagen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"2ac7786d-823c-4dd0-81d9-e09582263617\",\"title\":\"Der/Die Lernende kann Verben mit Akkusativ- und Dativobjekt verwenden.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; b) Geschäftspräsentation &gt; 3. Problembewältigung</p><p>Instructions can be found in the attached trainer notes in the classroom.</p>\",\"sessionDetails\":{\"id\":4497,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612782000,\"endTime\":1612783800,\"course\":612}},{\"unitId\":\"98ab0bad-d153-4fbd-bcb6-d5baef774ba9\",\"title\":\"Gesprächsführung\",\"activityDetails\":{\"id\":\"12e9a4f4-96ef-4faf-89c8-3bba8e80b8e3\",\"title\":\"Gesprächsführung\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"cc6897b8-efa7-4ae6-8ae5-b84ea07fffe1\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"8544e264-90d2-40e9-9eef-4a5d0aeea10d\",\"title\":\"Übung 1 \",\"type\":\"choice\"},{\"id\":\"1ab0ad5c-ea82-47de-a3a8-1c524e1f3a32\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"3a4150ca-55fa-42ab-8364-a0f408858be9\",\"title\":\"Übung 3\",\"type\":\"wordscategorizing\"},{\"id\":\"3c4fefa4-c9c4-461e-a9c3-2f692ae3db76\",\"title\":\"Übung 4\",\"type\":\"choice\"},{\"id\":\"5fec5a8e-046d-4782-b53d-432ec3b2f03c\",\"title\":\"Übung 5 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"d9abee97-e94e-4a80-b32f-405b1d155c4e\",\"title\":\"Übung 6\",\"type\":\"fillinthegapstext\"},{\"id\":\"ee118b0d-b443-4219-9a57-97ff227632ae\",\"title\":\"Übung 7\",\"type\":\"wordselector\"},{\"id\":\"fbd756e1-ac1f-498c-8652-7df4bdd74b0b\",\"title\":\"Übung 8 \",\"type\":\"fillinthegapstext\"},{\"id\":\"8e16ed8c-9993-472c-8724-fc79282b0e2e\",\"title\":\"Übung 9 (A) \",\"type\":\"sentence\"},{\"id\":\"4a38be80-2027-4185-a949-f84cab2b7497\",\"title\":\"Übung 9 (B) \",\"type\":\"sentence\"},{\"id\":\"03e680a5-c0e2-4d30-b6c6-5578ccc3dcbe\",\"title\":\"Übung 9 (C) \",\"type\":\"sentence\"}],\"vocabularyList\":null,\"totalExercises\":11,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"877d27db-f80a-43bc-84f2-3f67b1eef95e\",\"title\":\"Der/Die Lernende kann einfache Fragen stellen und darauf antworten, höflich unterbrechen und mit Unterbrechungen umgehen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"b2961591-991d-4134-8be1-7584fe91a8b2\",\"title\":\"Der/Die Lernende kann die Modalverben „können“ und „dürfen“ korrekt verwenden.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; b) Geschäftspräsentation &gt; 4. Gesprächsführung</p><p>Instructions can be found in the attached trainer notes in the classroom.</p>\",\"sessionDetails\":{\"id\":4498,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612868400,\"endTime\":1612870200,\"course\":612}},{\"unitId\":\"d5d820ad-9ebb-4810-9a5f-5818a2a12be3\",\"title\":\"Rückblick\",\"activityDetails\":{\"id\":\"7feb5b66-2d4a-4740-9c98-55ede86b767d\",\"title\":\"Rückblick\",\"type\":\"lesson\",\"description\":\"\",\"content_version\":\"1.0.1\",\"duration\":60,\"exercises\":[{\"id\":\"f50730df-c555-497a-a43c-681a0eede48a\",\"title\":\"Lernziele\",\"type\":\"index\"},{\"id\":\"b4d930b4-d7b6-41c3-9b26-784f1978065a\",\"title\":\"Übung 1 \",\"type\":\"fillinthegapsclick\"},{\"id\":\"c5c761be-c553-48d6-8f64-d94cedbe57f3\",\"title\":\"Übung 2 \",\"type\":\"fillinthegapsselect\"},{\"id\":\"2876f7c0-fdb6-482c-affd-f33f9df0c8dc\",\"title\":\"Übung 3 (A)\",\"type\":\"sentence\"},{\"id\":\"82539bf5-1920-4718-a108-02aa740c48d4\",\"title\":\"Übung 3 (B)\",\"type\":\"sentence\"},{\"id\":\"0d2eb3ee-c591-4815-8043-cd0a98d153e9\",\"title\":\"Übung 3 (C)\",\"type\":\"sentence\"},{\"id\":\"52615765-5f5f-4725-8ef7-01068914838f\",\"title\":\"Übung 4\",\"type\":\"choice\"},{\"id\":\"58fa7fb7-909f-429c-b243-fbeeb079ff90\",\"title\":\"Übung 5\",\"type\":\"fillinthegapsclick\"},{\"id\":\"62e54f7c-8c3c-4c9a-aff0-36fcb4f9dd87\",\"title\":\"Übung 6\",\"type\":\"fillinthegapsclick\"},{\"id\":\"bfd57cb6-826c-433f-a2ae-ac8fa02a667f\",\"title\":\"Übung 7 \",\"type\":\"wordselector\"},{\"id\":\"eaaf6757-edcc-41fe-9938-be39fb0bc2b7\",\"title\":\"Übung 8\",\"type\":\"fillinthegapstext\"},{\"id\":\"af6b9085-60c8-4014-be62-ed8ad5203705\",\"title\":\"Übung 9 (A)\",\"type\":\"fillinthegapstext\"},{\"id\":\"772c7d6c-fad3-41d9-aa72-6bbf57da7896\",\"title\":\"Übung 9 (B)\",\"type\":\"fillinthegapstext\"}],\"vocabularyList\":null,\"totalExercises\":12,\"completedExercises\":0},\"canDoStatements\":[{\"id\":\"b55505c1-4633-4abe-a749-e215f4133e02\",\"title\":\"Der/Die Lernende hat den Wortschatz und den Sprachgebrauch gemeistert, um auf A2.1-Niveau über Geschäftspräsentationen zu sprechen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]},{\"id\":\"03386295-6f6b-4386-9d39-735ae89974e7\",\"title\":\"Der/Die Lernende hat die Grammatik gemeistert, um auf A2.1-Niveau über Geschäftspräsentationen zu sprechen.\",\"description\":\"\",\"language\":\"DE-DE\",\"level\":\"A2.1\",\"languageTaught\":\"de-DE\",\"courseType\":\"Sprint Level German\",\"score\":[]}],\"trainerGuidence\":\"<p>Please use the following material:</p><p>German &gt; Sprint &gt; A2.1 &gt; Part A &gt; b) Geschäftspräsentation &gt; 5. Rückblick</p><p>Instructions can be found in the attached trainer notes in the classroom.</p>\",\"sessionDetails\":{\"id\":4499,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1612954800,\"endTime\":1612956600,\"course\":612}}]},{\"moduleId\":\"ca295938-5b04-481b-83e9-9abc321f28a8\",\"title\":\"Wiederholung\",\"level\":\"A2.1\",\"coursePart\":{\"id\":\"56862b4a-60ed-4c4b-ad76-a682a57fe6d4\",\"slug\":\"a\",\"title\":\"A\"},\"units\":[{\"unitId\":\"b8034de9-48e2-437f-a5e7-c012b13b7f8c\",\"title\":\"Wiederholung\",\"canDoStatements\":[],\"trainerGuidence\":\"<p>Nutzen Sie die Zeit, um die Inhalte des Kurses zu wiederholen oder auf die Schwierigkeiten der / des Lernenden einzugehen.</p>\",\"sessionDetails\":{\"id\":4500,\"status\":\"finished\",\"sessionType\":\"course\",\"trainingType\":\"oup_level\",\"startTime\":1613041200,\"endTime\":1613043000,\"course\":612}}]}]}"}}
    return JsonResponse(data)

def GetLearnerAssessments(request):
    data={"data":{"getLearnerAssessments":{"statusCode":200,"body":"{\"Items\":[]}","Message":"null","errorMessage":"null","errorType":"null","userSelectedCourses":"null"}}}
    return JsonResponse(data)


































# from django.shortcuts import render, redirect
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse,HttpResponseRedirect
# from polls.models import Person
# import tempfile
# from django.core.files.storage import FileSystemStorage
# from django.http import FileResponse
# import io
# import base64
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import openpyxl
# from django.http import HttpResponse
# from openpyxl import Workbook
# from django.http import JsonResponse
# from django.core import serializers
# from django.http import JsonResponse
# from django.db import models 
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# from asgiref.sync import sync_to_async
# matplotlib.use('agg')
# def samples(self):
#     data={"bhuvan":{"Username":"Bhuvan","Password":"python@95813"},"sai":{"Username":"sai","Password":"sai@95813"},
#           "mani":{"Username":"mani","Password":"mani@95813"},"raja":{"Username":"raja","Password":"raja@95813"},
#           "sathish":{"Username":"sathish","Password":"sathish@95813"},"chandra":{"Username":"chandra","Password":"chandra@95813"},
#           "rani":{"Username":"rani","Password":"rani@95813"},"kavya":{"Username":"kavya","Password":"kavya@95813"}}

#     return JsonResponse(data)

# def generate_excel(request):
#     # Create a new Excel workbook and add a worksheet
#     wb = openpyxl.Workbook()
#     ws1 = wb.active

#     # Write data to the first worksheet
#     ws1['A1'] = 'Name'
#     ws1['B1'] = 'Age'
#     ws1['A2'] = 'Alice'
#     ws1['B2'] = 25
#     ws1['A3'] = 'Bob'
#     ws1['B3'] = 30

#     # Create a new worksheet and write data to it
#     ws2 = wb.create_sheet('Data')
#     ws2['A1'] = 'Category'
#     ws2['B1'] = 'Value'
#     ws2['A2'] = 'Category 1'
#     ws2['B2'] = 10
#     ws2['A3'] = 'Category 2'
#     ws2['B3'] = 20

#     # Save the workbook to a temporary file
#     with tempfile.NamedTemporaryFile(delete=True, suffix='.xlsx') as tmp:
#         wb.save(tmp.name)

#         # Prompt the user to choose the download location
#         fs = FileSystemStorage()
#         filename = fs.save('myfile.xlsx', open(tmp.name, 'rb'))

#         # Serve the file as a response
#         response = FileResponse(fs.open(filename), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#         response['Content-Disposition'] = f'attachment; filename="{filename}"'

#     return response




# def mat(request):

#     return render(request, 'mat.html')


# @sync_to_async
# def create_chart():
#     data = {'apples': 10, 'oranges': 15, 'bananas': 5, 'pears': 20}

#     labels = np.array(list(data.keys()))
#     values = np.array(list(data.values()))

#     fig = plt.figure(figsize=(8, 6), dpi=80)
#     plt.bar(labels, values)
#     plt.title("Fruit Sales")
#     plt.xlabel("Fruit")
#     plt.ylabel("Number of Sales")

#     return fig

# async def barchart(request):
#     fig = await create_chart()

#     canvas = FigureCanvas(fig)
#     canvas.draw()

#     image = canvas.tostring_rgb()

#     context = {
#         'image': image
#     }

#     return render(request, 'mat.html', context)


# def registration(request):
    
#     return render(request, 'registrationform.html')
# def latest(request):
#     last_person = Person.objects.all()
#     print(last_person)
#     return render(request, 'latest.html')
    

# def test(request):
#     data=Person.objects.all()
#     person = Person(first_name='Ravi', last_name="Mahesh", email_address='ravi@gmail.com',password='ravi',cpassword='ravi')
#     person.save()
#     Person.objects.filter(first_name="Kavya Ravi").delete()
#     print(data)
#     return render(request, 'test.html',{"data":data})

# def user_name(request, user_name):
#     # Retrieve the corresponding User object from the database using the user_id argument
#     dict={"bhuvan":{"Username":"Bhuvan","Password":"python@95813"},"sai":{"Username":"sai","Password":"sai@95813"},
#           "mani":{"Username":"mani","Password":"mani@95813"},"raja":{"Username":"raja","Password":"raja@95813"},
#           "sathish":{"Username":"sathish","Password":"sathish@95813"},"chandra":{"Username":"chandra","Password":"chandra@95813"},
#           "rani":{"Username":"rani","Password":"rani@95813"},"kavya":{"Username":"kavya","Password":"kavya@95813"}}
    
#     # Perform any necessary processing on the User object
#     # ...
#     data=["kavya","ravi","raja"]
#     # Render the user_detail.html template and pass it a dictionary of context variables
#     return render(request, 'count.html', {'users':dict,"data":data})

# def user_detail(request, user_name):
#     user = "Bhuvan kumar"
#     return render(request, 'count.html', {'user': user})


# def count(request,id):
#     print(id)
#     return render(request,"count.html")

# def employess(self):
#     data={"status":"success","data":[{"id":1,"employee_name":"Tiger Nixon","employee_salary":320800,"employee_age":61,"profile_image":""},{"id":2,"employee_name":"Garrett Winters","employee_salary":170750,"employee_age":63,"profile_image":""},{"id":3,"employee_name":"Ashton Cox","employee_salary":86000,"employee_age":66,"profile_image":""},{"id":4,"employee_name":"Cedric Kelly","employee_salary":433060,"employee_age":22,"profile_image":""},{"id":5,"employee_name":"Airi Satou","employee_salary":162700,"employee_age":33,"profile_image":""},{"id":6,"employee_name":"Brielle Williamson","employee_salary":372000,"employee_age":61,"profile_image":""},{"id":7,"employee_name":"Herrod Chandler","employee_salary":137500,"employee_age":59,"profile_image":""},{"id":8,"employee_name":"Rhona Davidson","employee_salary":327900,"employee_age":55,"profile_image":""},{"id":9,"employee_name":"Colleen Hurst","employee_salary":205500,"employee_age":39,"profile_image":""},{"id":10,"employee_name":"Sonya Frost","employee_salary":103600,"employee_age":23,"profile_image":""},{"id":11,"employee_name":"Jena Gaines","employee_salary":90560,"employee_age":30,"profile_image":""},{"id":12,"employee_name":"Quinn Flynn","employee_salary":342000,"employee_age":22,"profile_image":""},{"id":13,"employee_name":"Charde Marshall","employee_salary":470600,"employee_age":36,"profile_image":""},{"id":14,"employee_name":"Haley Kennedy","employee_salary":313500,"employee_age":43,"profile_image":""},{"id":15,"employee_name":"Tatyana Fitzpatrick","employee_salary":385750,"employee_age":19,"profile_image":""},{"id":16,"employee_name":"Michael Silva","employee_salary":198500,"employee_age":66,"profile_image":""},{"id":17,"employee_name":"Paul Byrd","employee_salary":725000,"employee_age":64,"profile_image":""},{"id":18,"employee_name":"Gloria Little","employee_salary":237500,"employee_age":59,"profile_image":""},{"id":19,"employee_name":"Bradley Greer","employee_salary":132000,"employee_age":41,"profile_image":""},{"id":20,"employee_name":"Dai Rios","employee_salary":217500,"employee_age":35,"profile_image":""},{"id":21,"employee_name":"Jenette Caldwell","employee_salary":345000,"employee_age":30,"profile_image":""},{"id":22,"employee_name":"Yuri Berry","employee_salary":675000,"employee_age":40,"profile_image":""},{"id":23,"employee_name":"Caesar Vance","employee_salary":106450,"employee_age":21,"profile_image":""},{"id":24,"employee_name":"Doris Wilder","employee_salary":85600,"employee_age":23,"profile_image":""}],"message":"Successfully! All records has been fetched."}

#     return JsonResponse(data)













# def my_views(request):
#     array = ["Bhuvan","kumar","raja","rani"]
#     return render(request, 'my_template.html', {'array': array})

# def new_Sample(request):
#     data={"user1":"mani","user2":"sannu","user3":"bhunu"}
#     return render(request,"dropdown.html",context={"mydata":data})

# def mag(request,names):
#     name="welcome"
#     return render(request,"sample1.html",context={"mydata":names})

# def welcome(request,name):
#     if name=="mani":
#         return render(request,"mani.html")
#     if name=="sannu":
#         return render(request,"sannu.html")
#     if name=="bhunu":
#         return render(request,"bhunu.html")
#     else:
#         return render(request,"error.html")


# def sample(request):
#     return render(request, "sample.html")


# # Create your views here.
# def submit_form(request):
#      return render(request, "thankyou.html")
# def error(request):
# 	return render(request, "error.html")

# def contact(request):
   
#     mydict={"username":"Bhuvan104","password":"python@95813"}
#     print(type(mydict))
#     form=ContactForm()
#     return render(request,"contact.html",{'form':form,'mydict':mydict})




# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .forms import ContactForm

# @csrf_exempt
# def reg(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Get cleaned data from the form
#             data = form.cleaned_data
#             # Do something with the data, such as saving it to the database
#             # ...
#             # Return a success response
#             return JsonResponse({'status': 'success', 'message': 'Registration successful'})
#         else:
#             # Return a form errors response
#             errors = form.errors.as_json()
#             return JsonResponse({'status': 'error', 'errors': errors})
#     else:
#         # Return the form as HTML for a GET request
#         form = ContactForm()
#         return JsonResponse({'form': str(form)}, safe=False)


# def reg1(request):
#     print("welcome to chennai")
#     form = ContactForm()
#     serialized_form = serializers.serialize('json', [form, ])
#     return JsonResponse(serialized_form, safe=False)



# def my_data(request):
#     data={"emailid":"bhuvan@gmail.com",
#     "password":"python@95813"
#     }
#     return JsonResponse(data)


# def my_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             data = {'success': True}
#         else:
#             data = {'success': False, 'errors': form.errors}
#     else:
#         form = ContactForm()

#     return JsonResponse(data)
# # def details(request):
# #     form = Person.objects.all()
    
# #     dict={}
# #     for i in form:
# #         dict[i.id]={
# #         "first_name":i.first_name,
# #         "last_name":i.last_name,
# #         "password":i.password,
# #         "cpassword":i.cpassword
# #         }
# #     context = {'form':form}
    
# #     return render(request, 'delete.html', context)


# def delete(request, id):
#   member = Person.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect('/details')

# # from django.shortcuts import render
# # from json import dumps


# # def send_dictionary(request):
# # 	# create data dictionary
# # 	dataDictionary = {
# # 		'hello': 'World',
# # 		'geeks': 'forgeeks',
# # 		'ABC': 123,
# # 		456: 'abc',
# # 		14000605: 1,
# # 		'list': ['geeks', 4, 'geeks'],
# # 		'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
# # 	}
# # 	# dump data
# # 	dataJSON = dumps(dataDictionary);jsonresp=JsonResponse(dataDictionary);print(jsonresp)
# # 	return render(request, 'jso.html', {'data': dataJSON})

def GetLearnerAssessments(request):
    data={"username":"Bhuvan kumar"}
    return JsonResponse(data)