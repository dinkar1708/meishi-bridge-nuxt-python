# 📱 Mobile App - Flutter

**MeishiBridge Mobile Application**

Cross-platform mobile app for iOS and Android built with Flutter.

---

## 📋 Overview

The mobile app provides native mobile experience with:
- Camera-based business card scanner (OCR)
- NFC tap-to-share functionality
- Push notifications
- Biometric authentication
- Apple Wallet / Google Wallet integration
- Dark mode support
- Online-only (requires internet connection)

---

## 🛠️ Tech Stack

- **[Flutter](https://flutter.dev)** - Cross-platform framework
- **[Dart](https://dart.dev)** - Programming language
- **[Riverpod](https://riverpod.dev)** - State management
- **[Dio](https://pub.dev/packages/dio)** - HTTP client
- **[Flutter Secure Storage](https://pub.dev/packages/flutter_secure_storage)** - Secure token storage
- **[Camera](https://pub.dev/packages/camera)** - Camera access
- **[NFC Manager](https://pub.dev/packages/nfc_manager)** - NFC support
- **[Flutter i18n](https://pub.dev/packages/flutter_localizations)** - Internationalization

---

## 📂 Project Structure

```
mobile/
├── android/             # Android native code
├── ios/                 # iOS native code
├── lib/
│   ├── main.dart       # App entry point
│   │
│   ├── core/           # Core functionality
│   │   ├── config/
│   │   ├── constants/
│   │   ├── theme/
│   │   └── utils/
│   │
│   ├── data/           # Data layer
│   │   ├── models/
│   │   ├── repositories/
│   │   └── services/
│   │       ├── api_service.dart
│   │       ├── storage_service.dart
│   │       └── auth_service.dart
│   │
│   ├── domain/         # Business logic
│   │   ├── entities/
│   │   └── usecases/
│   │
│   ├── presentation/   # UI layer
│   │   ├── screens/
│   │   │   ├── auth/
│   │   │   ├── dashboard/
│   │   │   ├── editor/
│   │   │   └── scanner/
│   │   ├── widgets/
│   │   └── providers/
│   │
│   └── l10n/           # Localization
│       ├── app_ja.arb  # Japanese
│       └── app_en.arb  # English
│
├── test/               # Unit tests
├── integration_test/   # Integration tests
├── pubspec.yaml        # Dependencies
└── README.md           # This file
```

---

## 🚀 Getting Started

### **Prerequisites**

**Recommended:**
- **Flutter SDK 3.24+** (Latest Stable)
- **Dart SDK 3.5+** (Comes with Flutter)
- Android Studio (for Android development)
- Xcode 15+ (for iOS development, macOS only)

**Check your Flutter version:**
```bash
flutter --version
# Should show Flutter 3.24.x or higher

# Upgrade to latest stable
flutter upgrade
```

### **Installation**

```bash
# Navigate to mobile directory
cd mobile

# Check Flutter setup
flutter doctor

# Install dependencies
flutter pub get

# Run code generation (if using freezed/json_serializable)
flutter pub run build_runner build --delete-conflicting-outputs
```

---

## 🌍 Environment Configuration

The project supports **4 environments**:

| Environment | Purpose | Config File | API URL |
|-------------|---------|-------------|---------|
| **local** | Local development | `env_local.dart` | `http://localhost:8000` |
| **dev** | Development deployment | `env_dev.dart` | Dev API |
| **stg** | Staging/Testing | `env_stg.dart` | Staging API |
| **prod** | Production (Client) | `env_prod.dart` | Production API |

### **Setup Environment Files**

Create environment config files in `lib/core/config/`:

**`lib/core/config/env_local.dart`** (Local development)
```dart
class Environment {
  static const String apiUrl = 'http://localhost:8000/api/v1';
  static const String appUrl = 'http://localhost:3000';
  static const String env = 'local';
  static const bool isDev = true;
}
```

**`lib/core/config/env_dev.dart`** (Development deployment)
```dart
class Environment {
  static const String apiUrl = 'https://meishibridge-api-dev.onrender.com/api/v1';
  static const String appUrl = 'https://meishibridge-dev.vercel.app';
  static const String env = 'dev';
  static const bool isDev = true;
}
```

**`lib/core/config/env_stg.dart`** (Staging deployment)
```dart
class Environment {
  static const String apiUrl = 'https://meishibridge-api-stg.onrender.com/api/v1';
  static const String appUrl = 'https://meishibridge-stg.vercel.app';
  static const String env = 'stg';
  static const bool isDev = true;
}
```

**`lib/core/config/env_prod.dart`** (Production for clients)
```dart
class Environment {
  static const String apiUrl = 'https://meishibridge-api.onrender.com/api/v1';
  static const String appUrl = 'https://meishibridge.com';
  static const String env = 'prod';
  static const bool isDev = false;
}
```

### **Run with Environment**

```bash
# Local development (default)
flutter run

# Run with specific environment
flutter run --dart-define=ENV=dev
flutter run --dart-define=ENV=stg
flutter run --dart-define=ENV=prod

# Build for specific environment
flutter build apk --dart-define=ENV=prod
flutter build ios --dart-define=ENV=prod
```

---

## 💾 Data Strategy

**Online-Only Approach** (MVP simplification)

The app requires **active internet connection** and fetches data directly from the API.

### **Why Online-Only for MVP?**
- ✅ Simpler architecture
- ✅ Faster development
- ✅ No sync conflicts
- ✅ Always fresh data from server

### **Secure Token Storage**

**flutter_secure_storage** - JWT Tokens only:
```dart
// Store JWT token securely
await secureStorage.write(key: 'jwt_token', value: token);

// Retrieve token for API calls
final token = await secureStorage.read(key: 'jwt_token');
```

### **Data Flow**
```
User Action → API Call → Display Result
(No local database, direct API communication)
```

**Note:** Offline mode with local database can be added in Phase 2 if needed.

---

## 📱 Running the App

### **Development**

```bash
# Run on connected device
flutter run

# Run on specific device
flutter devices
flutter run -d <device_id>

# Run on iOS simulator
flutter run -d iPhone

# Run on Android emulator
flutter run -d emulator-5554

# Hot reload: Press 'r'
# Hot restart: Press 'R'
```

### **Build**

**Android APK:**
```bash
flutter build apk --release
# Output: build/app/outputs/flutter-apk/app-release.apk
```

**Android App Bundle (for Play Store):**
```bash
flutter build appbundle --release
# Output: build/app/outputs/bundle/release/app-release.aab
```

**iOS IPA (requires macOS):**
```bash
flutter build ios --release
# Then archive in Xcode
```

---

## 📱 Features

For complete feature list and roadmap, see **[Main README](../README.md#features)**.

---

## 📦 Dependencies

### **Core**
```yaml
dependencies:
  flutter:
    sdk: flutter

  # State Management
  flutter_riverpod: ^2.4.9

  # Networking
  dio: ^5.4.0

  # Secure Storage (JWT tokens only)
  flutter_secure_storage: ^9.0.0

  # Biometric Authentication
  local_auth: ^2.1.7

  # UI
  google_fonts: ^6.1.0
  flutter_svg: ^2.0.9

  # i18n
  flutter_localizations:
    sdk: flutter
  intl: ^0.18.1

  # Camera & OCR
  camera: ^0.10.5
  image_picker: ^1.0.5
  google_ml_kit: ^0.15.0

  # NFC
  nfc_manager: ^3.3.0

  # Utilities
  path_provider: ^2.1.1
  url_launcher: ^6.2.2
  share_plus: ^7.2.1
```

### **Dev Dependencies**
```yaml
dev_dependencies:
  flutter_test:
    sdk: flutter

  # Code Generation
  build_runner: ^2.4.7
  freezed: ^2.4.6
  json_serializable: ^6.7.1

  # Linting
  flutter_lints: ^3.0.1
```

---

## 🧪 Testing

### **Unit Tests**
```bash
# Run all tests
flutter test

# Run with coverage
flutter test --coverage

# Run specific test
flutter test test/services/api_service_test.dart
```

### **Widget Tests**
```bash
flutter test test/widgets/
```

### **Integration Tests**
```bash
flutter test integration_test/
```

---

## 🎨 Design

### **Theme**
- Light mode (default)
- Dark mode (auto or manual)
- Japanese-friendly fonts (Noto Sans JP)

### **Colors**
```dart
// Primary
Color primaryColor = Color(0xFF3B82F6);

// Secondary
Color secondaryColor = Color(0xFF6B7280);

// Success
Color successColor = Color(0xFF10B981);

// Error
Color errorColor = Color(0xFFEF4444);
```

### **Typography**
```dart
// Headings: Noto Sans JP (Bold)
// Body: Noto Sans JP (Regular)
// Code: Fira Code
```

---

## 🌍 Localization (i18n)

**Supported Languages:** English & Japanese only (for now)

### **Setup (Flutter Intl)**

**1. Add dependencies:**
```yaml
# pubspec.yaml
dependencies:
  flutter_localizations:
    sdk: flutter
  intl: ^0.18.1

flutter:
  generate: true  # Enable code generation
```

**2. Configure l10n:**
```yaml
# l10n.yaml
arb-dir: lib/l10n
template-arb-file: app_en.arb
output-localization-file: app_localizations.dart
```

### **Translation Files (ARB)**

**`lib/l10n/app_ja.arb`** (Japanese)
```json
{
  "@@locale": "ja",
  "appTitle": "メイシブリッジ",
  "login": "ログイン",
  "register": "新規登録",
  "save": "保存",
  "cancel": "キャンセル",
  "name": "氏名",
  "company": "会社名",
  "title": "役職"
}
```

**`lib/l10n/app_en.arb`** (English - Template)
```json
{
  "@@locale": "en",
  "appTitle": "MeishiBridge",
  "login": "Login",
  "register": "Sign Up",
  "save": "Save",
  "cancel": "Cancel",
  "name": "Name",
  "company": "Company",
  "title": "Title"
}
```

### **Usage in Flutter**

**1. Configure MaterialApp:**
```dart
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

MaterialApp(
  localizationsDelegates: [
    AppLocalizations.delegate,
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  supportedLocales: [
    Locale('en', ''),  // English
    Locale('ja', ''),  // Japanese
  ],
  locale: Locale('ja'),  // Default: Japanese
);
```

**2. Use in widgets:**
```dart
// Get translations
final l10n = AppLocalizations.of(context)!;

Text(l10n.login),      // "ログイン" or "Login"
Text(l10n.save),       // "保存" or "Save"
Text(l10n.appTitle),   // "メイシブリッジ" or "MeishiBridge"
```

**3. Generate code:**
```bash
# After editing ARB files, run:
flutter gen-l10n
```

**Future:** More languages can be added in Phase 2/3 if needed.

---

## 📱 Platform-Specific Setup

### **iOS Setup**

**1. Minimum iOS Version:**
Edit `ios/Podfile`:
```ruby
platform :ios, '13.0'
```

**2. Camera Permissions:**
Edit `ios/Runner/Info.plist`:
```xml
<key>NSCameraUsageDescription</key>
<string>We need camera access to scan business cards</string>

<key>NSPhotoLibraryUsageDescription</key>
<string>We need photo library access to save cards</string>
```

**3. NFC Permissions:**
```xml
<key>NFCReaderUsageDescription</key>
<string>We need NFC to share business cards</string>
```

### **Android Setup**

**1. Minimum SDK:**
Edit `android/app/build.gradle`:
```gradle
minSdkVersion 21
targetSdkVersion 34
```

**2. Permissions:**
Edit `android/app/src/main/AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.NFC" />
<uses-permission android:name="android.permission.INTERNET" />
```

---

## 🚢 Deployment

### **iOS (App Store)**

1. **Setup:**
   - Apple Developer account ($99/year)
   - App Store Connect
   - Signing certificates

2. **Build:**
   ```bash
   flutter build ios --release
   ```

3. **Archive in Xcode:**
   - Open `ios/Runner.xcworkspace`
   - Product → Archive
   - Upload to App Store Connect

4. **TestFlight:**
   - Beta testing before release

### **Android (Play Store)**

1. **Setup:**
   - Google Play Console account ($25 one-time)
   - Keystore for signing

2. **Create Keystore:**
   ```bash
   keytool -genkey -v -keystore meishilink.jks \
     -keyalg RSA -keysize 2048 -validity 10000 \
     -alias meishilink
   ```

3. **Build:**
   ```bash
   flutter build appbundle --release
   ```

4. **Upload:**
   - Upload to Play Console
   - Internal testing → Beta → Production

---

## 🔧 Development Tips

### **Hot Reload**
```bash
# In terminal while app is running:
# r - Hot reload
# R - Hot restart
# q - Quit
```

### **Debugging**
```bash
# Enable debug logging
flutter run --debug

# Performance profiling
flutter run --profile

# Enable verbose logging
flutter run -v
```

### **Code Generation**
```bash
# Generate code (freezed, json_serializable)
flutter pub run build_runner build --delete-conflicting-outputs

# Watch mode (auto-generate)
flutter pub run build_runner watch
```

---

## 🔍 Troubleshooting

### **iOS Build Fails**
```bash
cd ios
pod deintegrate
pod install
cd ..
flutter clean
flutter pub get
```

### **Android Build Fails**
```bash
cd android
./gradlew clean
cd ..
flutter clean
flutter pub get
```

### **Plugin Issues**
```bash
flutter pub cache repair
flutter pub get
```

---

## 📚 Resources

- [Flutter Documentation](https://flutter.dev/docs)
- [Dart Language Tour](https://dart.dev/guides/language/language-tour)
- [Riverpod Documentation](https://riverpod.dev)
- [Material Design](https://material.io/design)

---

## 🗓️ Roadmap

**Phase 1:** (Current)
- Project setup
- Basic UI structure

**Phase 2:**
- API integration
- Authentication

**Phase 3:**
- Card CRUD
- Camera scanner

**Phase 4:**
- NFC support
- Wallet integration

---

## 🤝 Contributing

See main [README](../README.md) for contribution guidelines.

---

**Built with Flutter** 💙
