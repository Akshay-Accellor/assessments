Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-07: Sections Configuration in Contentful', () => {
    before(async () => { await browser.url('https://app.contentful.com'); });
    it('Positive - Verify sections can be configured separately in Contentful', async () => {
        const dashboard = await $('.dashboard');
        await expect(dashboard).toBeDisplayed();
        const sectionSelect = await $('.section-select');
        await sectionSelect.click();
        const saveChanges = await $('.save-changes');
        await saveChanges.click();
        const previewMode = await $('.preview-mode');
        await expect(previewMode).toBeDisplayed();
    });
    it('Negative - Verify configuration fails without permissions', async () => {
        const saveChanges = await $('.save-changes');
        await saveChanges.click();
        const errorMessage = await $('.error-message');
        await expect(errorMessage).toBeDisplayed();
    });
    it('Edge - Verify configuration of multiple sections at once', async () => {
        const sectionSelect1 = await $('.section-select1');
        await sectionSelect1.click();
        const sectionSelect2 = await $('.section-select2');
        await sectionSelect2.click();
        const saveChanges = await $('.save-changes');
        await saveChanges.click();
        const previewMode = await $('.preview-mode');
        await expect(previewMode).toBeDisplayed();
    });
});
