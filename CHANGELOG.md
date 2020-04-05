# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Added
- Django 2.1-3.0 support

## [0.3.0] - 2018-02-04

### Added
- Django 1.11-2.0 support
- Python 3.6 support

### Changed
- FIX: Use `@add_metaclass()` decorator from `six` so that `testRender200s()` and `testRenderAPI200s()` are generated in Python 3

## [0.2.0] - 2017-03-02

### Added
- Add `testRenderAPI200s()` test method which gets created when `getAPI200s()` is defined

### Changed
- FIX: Use `None` as default instead of `{}` to prevent memory reuse issues

## [0.1.1] - 2017-01-11

### Changed
- FIX: Add `url` and `tests` packages to setup.py

## [0.1.0] - 2017-01-11

### Added
- Initial test utilities including `RenderTestCaseMixin`, `RenderTestCase`, and `RenderTransactionTestCase`
- Django 1.8-1.10 support
- Python 2.7, 3.4-3.5 support
